import os
import subprocess
from pathlib import Path
import sys

def create_message_filter():
    """Create message translation mapping file"""
    translations = {
        # Original translations
        "株価データが正常に表示され、グラフやテクニカル指標が更新されているか確認できますか？": "feat: Update stock price display and technical indicators",
        "株価の監視アプリケーションが正常に動作していますか？": "feat: Implement stock monitoring application",
        "アプリケーションは正常に再起動され、株価のグラフとトレンド情報が表示されていますか？": "feat: Add auto-restart and trend display",
        "アプリケーションは正常に動作していますか？": "feat: Implement application monitoring",
        "アプリケーションは正常に起動し、株価のグラフとトレンド情報が表示されていますか？": "feat: Add stock price graph and trend info",
        "株価チャートとテクニカル指標は正常に表示されていますか？": "feat: Implement stock chart and indicators",
        "移動平均線の期間を20日・50日から12日・26日に変更しました": "feat: Update moving average periods to 12/26 days",
        # Additional generic translations
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

def setup_git_config():
    """Configure git with provided credentials without prompting"""
    github_username = os.environ.get("GITHUB_USERNAME")
    github_email = os.environ.get("GITHUB_EMAIL")
    github_token = os.environ.get("GITHUB_TOKEN")

    if not all([github_username, github_email, github_token]):
        print("Error: GitHub credentials not found in environment")
        sys.exit(1)

    try:
        # Set git configuration without prompting
        subprocess.run(["git", "config", "user.name", github_username], check=True, capture_output=True)
        subprocess.run(["git", "config", "user.email", github_email], check=True, capture_output=True)

        # Configure credential helper to avoid prompts
        subprocess.run(["git", "config", "credential.helper", "store"], check=True, capture_output=True)

        return github_username, github_email, github_token
    except subprocess.CalledProcessError as e:
        print(f"Error configuring git: {e}")
        sys.exit(1)

def backup_repository():
    """Create a backup of the repository"""
    try:
        backup_path = Path("backup_repo")
        if backup_path.exists():
            subprocess.run(["rm", "-rf", str(backup_path)], check=True)
        subprocess.run(["cp", "-r", ".", str(backup_path)], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error creating backup: {e}")
        sys.exit(1)

def main():
    print("Starting repository history rewrite...")

    # Setup git configuration
    github_username, github_email, github_token = setup_git_config()

    # Create message filter file
    filter_path = create_message_filter()

    # Create the filter script
    filter_script = f"""
import os
def callback(commit):
    try:
        # Translate commit message
        msg = commit.message.decode('utf-8', errors='replace')
        with open("{filter_path}", "r", encoding="utf-8") as f:
            for line in f:
                if "=" in line:
                    jp, en = line.strip().split("=")
                    msg = msg.replace(jp, en)

        # Update commit information
        commit.message = msg.encode('utf-8')
        commit.author_name = b"{github_username}"
        commit.author_email = b"{github_email}"
        commit.committer_name = b"{github_username}"
        commit.committer_email = b"{github_email}"
    except Exception as e:
        print(f"Error processing commit: {{e}}")
        raise
    """

    try:
        with open("filter.py", "w", encoding="utf-8") as f:
            f.write(filter_script)

        print("Running git filter-repo...")
        # Run git filter-repo without prompting
        subprocess.run([
            "git", "filter-repo",
            "--force",
            "--commit-callback-script", "filter.py"
        ], check=True, capture_output=True)

        print("Updating remote...")
        # Setup remote with token authentication
        repo_url = f"https://{github_username}:{github_token}@github.com/mr-myself/stock-monitor-dashboard.git"

        # Force push changes without prompting
        subprocess.run(["git", "push", "-f", repo_url, "main"], check=True, capture_output=True)

        print("Successfully rewrote repository history and pushed changes")

    except subprocess.CalledProcessError as e:
        print(f"Error executing git commands: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()