import os
import subprocess
from pathlib import Path
import sys
import re

def create_message_filter():
    """Create message translation mapping file"""
    translations = {
        # Japanese to English translations for stock monitoring app
        "株価データが正常に表示され、グラフやテクニカル指標が更新されているか確認できますか？": "feat: Update stock price display and technical indicators",
        "株価の監視アプリケーションが正常に動作していますか？": "feat: Implement stock monitoring application",
        "アプリケーションは正常に再起動され、株価のグラフとトレンド情報が表示されていますか？": "feat: Add auto-restart and trend display",
        "アプリケーションは正常に動作していますか？": "feat: Implement application monitoring",
        "アプリケーションは正常に起動し、株価のグラフとトレンド情報が表示されていますか？": "feat: Add stock price graph and trend info",
        "株価チャートとテクニカル指標は正常に表示されていますか？": "feat: Implement stock chart and indicators",
        "移動平均線の期間を20日・50日から12日・26日に変更しました": "feat: Update moving average periods to 12/26 days",
        # Common Japanese commit messages
        "初期コミット": "feat: Initial commit",
        "バグ修正": "fix: Bug fixes",
        "機能追加": "feat: Add new features",
        "ドキュメント更新": "docs: Update documentation",
        "リファクタリング": "refactor: Code improvements",
        "テスト追加": "test: Add tests",
        "パフォーマンス改善": "perf: Performance improvements",
        "依存関係の更新": "chore: Update dependencies"
    }

    filter_path = Path("msg-filter.txt")
    try:
        with open(filter_path, "w", encoding="utf-8") as f:
            for jp, en in translations.items():
                f.write(f"{jp}={en}\n")
        return filter_path
    except IOError as e:
        print(f"Error creating message filter file: {e}")
        sys.exit(1)

def clean_repository():
    """Clean the repository and create a fresh branch"""
    try:
        # Reset to the first commit
        result = subprocess.run(
            ["git", "rev-list", "--max-parents=0", "HEAD"],
            capture_output=True,
            text=True,
            check=True
        )
        first_commit = result.stdout.strip()

        # Create a fresh branch from the first commit
        subprocess.run(["git", "checkout", "--orphan", "temp", first_commit], check=True, capture_output=True)
        subprocess.run(["git", "commit", "--amend", "--no-edit"], check=True, capture_output=True)

        return True
    except subprocess.CalledProcessError as e:
        print(f"Error cleaning repository: {e}")
        if hasattr(e, 'stderr'):
            print(f"Error details: {e.stderr}")
        sys.exit(1)

def setup_git():
    """Setup git configuration"""
    github_username = os.environ.get("GITHUB_USERNAME")
    github_email = os.environ.get("GITHUB_EMAIL")
    github_token = os.environ.get("GITHUB_TOKEN")

    if not all([github_username, github_email, github_token]):
        print("Error: GitHub credentials not found in environment")
        sys.exit(1)

    commands = [
        ["git", "config", "--global", "user.name", github_username],
        ["git", "config", "--global", "user.email", github_email],
        ["git", "config", "--global", "--add", "safe.directory", "/home/runner/workspace"],
    ]

    for cmd in commands:
        try:
            subprocess.run(cmd, check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command {' '.join(cmd)}: {e}")
            sys.exit(1)

    return github_username, github_email, github_token

def main():
    print("Starting repository history rewrite...")

    # Clean repository and create fresh branch
    clean_repository()

    # Setup git configuration
    github_username, github_email, github_token = setup_git()

    # Create message filter
    filter_path = create_message_filter()

    try:
        print("Running git filter-repo...")

        # Get the absolute path to git-filter-repo
        git_filter_repo_path = "/home/runner/workspace/.pythonlibs/bin/git-filter-repo"

        # Ensure the script exists and is executable
        if os.path.exists(git_filter_repo_path):
            os.chmod(git_filter_repo_path, 0o755)

        # Create the filter script
        with open("filter.py", "w", encoding="utf-8") as f:
            f.write(f'''
import re

def commit_callback(commit):
    try:
        # Skip unwanted commits
        msg = commit.message.decode('utf-8', errors='replace')
        if any(skip in msg.lower() for skip in ['agent query:', 'checkpoint after', 'contact927']):
            return False

        # Translate Japanese messages to English
        with open("{filter_path}", "r", encoding="utf-8") as f:
            for line in f:
                if "=" in line:
                    jp, en = line.strip().split("=")
                    msg = msg.replace(jp, en)

        # Clean up any remaining Japanese characters
        msg = re.sub(r'[\\u3000-\\u303f\\u3040-\\u309f\\u30a0-\\u30ff\\u4e00-\\u9faf\\u3400-\\u4dbf]', '', msg)
        msg = msg.strip()

        # Use default message if empty
        if not msg:
            msg = "feat: Update application"

        # Set commit information
        commit.message = msg.encode('utf-8')
        commit.author_name = b"{github_username}"
        commit.author_email = b"{github_email}"
        commit.committer_name = b"{github_username}"
        commit.committer_email = b"{github_email}"
        return True

    except Exception as e:
        print(f"Error processing commit: {{e}}")
        return False
''')

        # Run git filter-repo
        result = subprocess.run([
            git_filter_repo_path,
            "--force",
            "--commit-callback", "filter.py",
        ], capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Error running git-filter-repo:\n{result.stderr}")
            sys.exit(1)

        print("Setting up remote with token...")
        repo_url = f"https://{github_username}:{github_token}@github.com/mr-myself/stock-monitor-dashboard.git"

        # Force push changes
        subprocess.run(["git", "push", "-f", repo_url, "HEAD:main"], check=True, capture_output=True)

        print("Successfully rewrote repository history and pushed changes")

    except subprocess.CalledProcessError as e:
        print(f"Error executing git commands: {e}")
        if hasattr(e, 'stderr'):
            print(f"Error details: {e.stderr}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()