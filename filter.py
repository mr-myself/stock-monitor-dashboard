
import os
def callback(commit):
    try:
        # Translate commit message
        msg = commit.message.decode('utf-8', errors='replace')
        with open("msg-filter.txt", "r", encoding="utf-8") as f:
            for line in f:
                if "=" in line:
                    jp, en = line.strip().split("=")
                    msg = msg.replace(jp, en)

        # Update commit information
        commit.message = msg.encode('utf-8')
        commit.author_name = b"mr-myself"
        commit.author_email = b"keisuke@mr-myself.com"
        commit.committer_name = b"mr-myself"
        commit.committer_email = b"keisuke@mr-myself.com"
    except Exception as e:
        print(f"Error processing commit: {e}")
        raise
    