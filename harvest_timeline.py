import json
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = '4eALQBto0scBBfkyL55KvO0JP'
CONSUMER_SECRET = '7WasagTGUTzbSDuRtGnDyKKaxKkIj1nAyrCZqsahQeWEnZLlsY'
OAUTH_TOKEN = '16909452-dem1yh9b5lQfFqozEkhZicHQ7kongBsNs4y2r4HMB'
OAUTH_TOKEN_SECRET = '0YgvWmZWFlxBxbi8LJOTKlUrXivNdDuZSH2bEEVMPcYXo'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a tweet
    print status.text