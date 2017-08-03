import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter

CONSUMER_KEY = '4eALQBto0scBBfkyL55KvO0JP'
CONSUMER_SECRET = '7WasagTGUTzbSDuRtGnDyKKaxKkIj1nAyrCZqsahQeWEnZLlsY'
OAUTH_TOKEN = '16909452-dem1yh9b5lQfFqozEkhZicHQ7kongBsNs4y2r4HMB'
OAUTH_TOKEN_SECRET = '0YgvWmZWFlxBxbi8LJOTKlUrXivNdDuZSH2bEEVMPcYXo'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 150
query = 'London'

# Get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

min_retweets = 20

pop_tweets = [status
              for status in results
              if status._json['retweet_count'] > min_retweets]

# create a list of tweet tuples associating each tweet's text with its retweet count
tweet_tups = [(tweet._json['text'].encode('utf-8'), tweet._json['retweet_count'])
              for tweet in pop_tweets]

# Sort the tuple entries in descending order
most_popular_tups = sorted(tweet_tups, key = itemgetter(1), reverse=True)[:5]