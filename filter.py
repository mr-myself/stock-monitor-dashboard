
import re
def commit_callback(commit):
    msg = commit.message.decode('utf-8', errors='replace')
    with open("msg-filter.txt", "r", encoding="utf-8") as f:
        for line in f:
            if "=" in line:
                jp, en = line.strip().split("=")
                msg = msg.replace(jp, en)

    commit.message = msg.encode('utf-8')
    commit.author_name = b"mr-myself"
    commit.author_email = b"keisuke@mr-myself.com"
    commit.committer_name = b"mr-myself"
    commit.committer_email = b"keisuke@mr-myself.com"
