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

LON_WOE_ID = 44418
DUB_WOE_ID = 560743
PAR_WOE_ID = 615702

lon_trends = api.trends_place(LON_WOE_ID)
dub_trends = api.trends_place(DUB_WOE_ID)
par_trends = api.trends_place(PAR_WOE_ID)

dub_trends_set = set([trend['name']
                      for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name']
                      for trend in lon_trends[0]['trends']])

par_trends_set = set([trend['name']
                      for trend in par_trends[0]['trends']])

common_trends = set.intersection(dub_trends_set,lon_trends_set, par_trends_set)

print common_trends