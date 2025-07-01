import os
import tweepy
from dotenv import load_dotenv
import schedule
import time

load_dotenv()
API_KEY = os.getenv('API_KEY')
API_KEY_SECRET = os.getenv('API_KEY_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_KEY_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

tweets = [
    "Hello world! #This is an automated post",
    "Did you know you can automate your tweets? #Automation",
    "Follow me for more updates! #Sherry",
]
tweet_index = 0

def post_tweet(message):
    try:
        response = client.create_tweet(text=message)
        print(f'Tweet posted successfully! Tweet ID: {response.data["id"]}')
    except Exception as e:
        print(f'Error posting tweet: {e}')

def job():
    global tweet_index
    if tweet_index < len(tweets):
        post_tweet(tweets[tweet_index])
        tweet_index += 1
    else:
        print("All tweets have been posted. Stopping the bot.")
        exit()

if __name__ == '__main__':
    schedule.every(2).minutes.do(job)
    print("Bot started. Posting every 2 minutes.")
    while True:
        schedule.run_pending()
        time.sleep(1)
