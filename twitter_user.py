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

user = api.get_user('@Virunee')

print "Username: " + user.screen_name
print "Followers:" + str(user.followers_count)

i=1

for friend in user.friends():
    print
    print "Friend #" + str(i)
    print friend.screen_name
    print friend.followers_count
    i=i+1