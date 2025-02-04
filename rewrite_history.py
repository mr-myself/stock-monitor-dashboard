import os
import subprocess
from pathlib import Path

def create_message_filter():
    """Create message translation mapping file"""
    translations = {
        "株価データが正常に表示され、グラフやテクニカル指標が更新されているか確認できますか？": "feat: Update stock price display and technical indicators",
        "株価の監視アプリケーションが正常に動作していますか？": "feat: Implement stock monitoring application",
        "アプリケーションは正常に再起動され、株価のグラフとトレンド情報が表示されていますか？": "feat: Add auto-restart and trend display",
        "アプリケーションは正常に動作していますか？": "feat: Implement application monitoring",
        "アプリケーションは正常に起動し、株価のグラフとトレンド情報が表示されていますか？": "feat: Add stock price graph and trend info",
        "株価チャートとテクニカル指標は正常に表示されていますか？": "feat: Implement stock chart and indicators",
        "移動平均線の期間を20日・50日から12日・26日に変更しました": "feat: Update moving average periods to 12/26 days"
    }
    
    filter_path = Path("../msg-filter.txt")
    with open(filter_path, "w", encoding="utf-8") as f:
        for jp, en in translations.items():
            f.write(f"{jp}={en}\n")
    return filter_path

def main():
    # Backup repository
    subprocess.run(["cp", "-r", ".", "../backup_repo"], check=True)
    
    # Create message filter file
    filter_path = create_message_filter()
    
    # Configure git with environment variables
    github_username = os.environ.get("GITHUB_USERNAME")
    github_email = os.environ.get("GITHUB_EMAIL")
    
    filter_script = f"""
    import os
    def callback(commit):
        # Translate commit message
        msg = commit.message.decode('utf-8')
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
    """
    
    with open("../filter.py", "w") as f:
        f.write(filter_script)
    
    # Run git filter-repo
    subprocess.run([
        "git", "filter-repo",
        "--force",
        "--commit-callback-script", "../filter.py"
    ], check=True)
    
    # Update remote
    subprocess.run([
        "git", "remote", "add", "origin",
        "https://github.com/mr-myself/stock-monitor-dashboard.git"
    ], check=True)
    
    # Force push changes
    token = os.environ.get("GITHUB_TOKEN")
    repo_url = f"https://{github_username}:{token}@github.com/mr-myself/stock-monitor-dashboard.git"
    subprocess.run(["git", "push", "-f", repo_url, "main"], check=True)

if __name__ == "__main__":
    main()
