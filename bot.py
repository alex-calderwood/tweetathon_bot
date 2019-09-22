import tweepy
from cred import *
from datetime import datetime

# Step 1: Create a new Twitter account that will be responsible for posts

# Step 2: Go to the twitter application dashboard and press "Create an app".
# Here's the URL:
# https://developer.twitter.com/en/apps

# Step 3: Generate an access key, and Fill out the access token information in cred.py

# Step 4: Install tweepy
# pip install -r requirements.txt

# Step 5: Run this code
# python bot.py

# Step 6: Check out this quickstart guide and read the tweepy documentation
# https://realpython.com/twitter-bot-python-tweepy/


class TwitterBot:
    def __init__(self):
        # Authenticate to Twitter with the credentials in cred.py
        self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

        # Create API object
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def tweet(self, text):
        print('Sending tweet @ {}'.format(datetime.now()))
        print('\t' + text)
        self.api.update_status(text)


if __name__ == '__main__':
    bot = TwitterBot()

    # Send a test tweet
    bot.tweet("This tweet was automatically created...")