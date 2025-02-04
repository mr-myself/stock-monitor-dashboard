import os
import subprocess
from pathlib import Path
import sys

def create_message_filter():
    """Create message translation mapping file"""
    translations = {
        # Translations have been updated to English
        "feat: Update stock price display and technical indicators": "feat: Update stock price display and technical indicators",
        "feat: Implement stock monitoring application": "feat: Implement stock monitoring application",
        "feat: Add auto-restart and trend display": "feat: Add auto-restart and trend display",
        "feat: Implement application monitoring": "feat: Implement application monitoring",
        "feat: Add stock price graph and trend info": "feat: Add stock price graph and trend info",
        "feat: Implement stock chart and indicators": "feat: Implement stock chart and indicators",
        "feat: Update moving average periods to 12/26 days": "feat: Update moving average periods to 12/26 days",
        # Additional generic translations
        "feat: Initial commit": "feat: Initial commit",
        "fix: Bug fixes": "fix: Bug fixes",
        "feat: Add new features": "feat: Add new features",
        "docs: Update documentation": "docs: Update documentation",
        "refactor: Code improvements": "refactor: Code improvements",
        "test: Add tests": "test: Add tests",
        "perf: Performance improvements": "perf: Performance improvements",
        "chore: Update dependencies": "chore: Update dependencies"
    }

    filter_path = Path("msg-filter.txt")
    try:
        with open(filter_path, "w", encoding="utf-8") as f:
            for en_key, en_value in translations.items():
                f.write(f"{en_key}={en_value}\n")
        return filter_path
    except IOError as e:
        print(f"Error creating message filter file: {e}")
        sys.exit(1)

def initialize_repo():
    """Initialize git repository if needed"""
    try:
        # Initialize repository if not already initialized
        if not Path(".git").exists():
            subprocess.run(["git", "init"], check=True, capture_output=True)

        # Ensure we're on the main branch
        subprocess.run(["git", "checkout", "-B", "main"], check=True, capture_output=True)

        return True
    except subprocess.CalledProcessError as e:
        print(f"Error initializing repository: {e}")
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

    # Initialize repository
    initialize_repo()

    # Setup git configuration
    github_username, github_email, github_token = setup_git()

    # Create message filter file
    filter_path = create_message_filter()

    try:
        print("Running git filter-repo...")

        # Get the absolute path to git-filter-repo
        git_filter_repo_path = "/home/runner/workspace/.pythonlibs/bin/git-filter-repo"

        # Ensure the scripts exist and are executable
        for script in [git_filter_repo_path]:
            if os.path.exists(script):
                os.chmod(script, 0o755)

        # Create the filter script
        with open("filter.py", "w", encoding="utf-8") as f:
            f.write(f'''
import re
def commit_callback(commit):
    msg = commit.message.decode('utf-8', errors='replace')
    with open("{filter_path}", "r", encoding="utf-8") as f:
        for line in f:
            if "=" in line:
                jp, en = line.strip().split("=")
                msg = msg.replace(jp, en)

    commit.message = msg.encode('utf-8')
    commit.author_name = b"{github_username}"
    commit.author_email = b"{github_email}"
    commit.committer_name = b"{github_username}"
    commit.committer_email = b"{github_email}"
''')

        # Run git filter-repo with absolute path
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
        subprocess.run(["git", "push", "-f", repo_url, "main"], check=True, capture_output=True)

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