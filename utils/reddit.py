import os
from dotenv import load_dotenv
import praw
import json

load_dotenv()

class Reddit:
    def __init__(self):
        """
        Initialize Reddit API
        """
        print("[+] Initializing Reddit API...")
        self.reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_SECRET"),
            user_agent=f"persona-creator-agent/0.1 by u/{os.getenv('REDDIT_USERNAME')}"
        )

    def get_user_comments(self, username):
        """
        Retrieve the user's comments from Reddit
        """
        print("[+] Retrieving user comments...")
        user = self.reddit.redditor(username)
        comments_json = []

        for comment in user.comments.new(limit=None):
            comments_json.append({
                # "id": comment.id,
                "body": comment.body,
                "subreddit": str(comment.subreddit),
                # "score": comment.score,
                # "created_utc": comment.created_utc,
                # "permalink": f"https://reddit.com{comment.permalink}"
            })
        print(f'[+] Retrieved {len(comments_json)} comments from {username}')
        return comments_json

reddit = Reddit()


