# Reddit Bot

made this to auto-post to r/minecraft when i upload cool builds. still learning the api so it crashes sometimes lol

## what it does

- posts screenshots from a folder automatically
- adds title with build name
- tries to avoid duplicate posts (not perfect)

## setup

```bash
pip install praw python-dotenv
```

make a `.env` file with:
```
REDDIT_CLIENT_ID=your_id_here
REDDIT_CLIENT_SECRET=your_secret_here
REDDIT_USERNAME=your_username
REDDIT_PASSWORD=your_password
SUBREDDIT=minecraft
```

## run it

```bash
python bot.py
```

## known issues

- sometimes posts the same thing twice if you interrupt it
- rate limit errors happen if you run it too fast
- image format detection is kinda broken for .webp files

todo: add support for imgur uploads since reddit compression sucks
