import os
import praw
from dotenv import load_dotenv
import time

load_dotenv()

# setup reddit client
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent="minecraft_poster_bot/1.0 by u/" + os.getenv("REDDIT_USERNAME")
)

def get_screenshots(folder="./screenshots"):
    """get all images from folder"""
    valid_extensions = [".png", ".jpg", ".jpeg"]
    files = []
    
    for f in os.listdir(folder):
        if any(f.lower().endswith(ext) for ext in valid_extensions):
            files.append(os.path.join(folder, f))
    
    return files

def post_to_reddit(image_path, title):
    """submit image to subreddit"""
    try:
        subreddit = reddit.subreddit(os.getenv("SUBREDDIT", "minecraft"))
        submission = subreddit.submit_image(title, image_path=image_path)
        print(f"posted: {submission.shortlink}")
        return True
    except Exception as e:
        print(f"error posting: {e}")
        return False

def main():
    screenshots = get_screenshots()
    
    if not screenshots:
        print("no screenshots found in ./screenshots folder")
        return
    
    print(f"found {len(screenshots)} screenshots")
    
    for screenshot in screenshots:
        filename = os.path.basename(screenshot)
        # use filename as title (remove extension)
        title = os.path.splitext(filename)[0]
        
        print(f"posting {filename}...")
        success = post_to_reddit(screenshot, title)
        
        if success:
            # move to posted folder so we dont repost
            os.makedirs("./posted", exist_ok=True)
            os.rename(screenshot, f"./posted/{filename}")
        
        # wait to avoid rate limits
        time.sleep(30)

if __name__ == "__main__":
    main()
