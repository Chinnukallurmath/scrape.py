import praw
from praw import Reddit
reddit = praw.Reddit(
    client_id="YOUR_ID",
    client_secret="YOUR_SECRET",
    user_agent="summarizer"
)

def get_reddit_text(url):
    try:
        submission = reddit.submission(url=url)
        text = submission.title + "\n" + submission.selftext
        submission.comments.replace_more(limit=0)
        comments = "\n".join([comment.body for comment in submission.comments[:5]])
        return text + "\nComments:\n" + comments
    except Exception as e:
        print(f"Reddit error: {e}")
        return None
