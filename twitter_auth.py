import tweepy
from tweepy import OAuthHandler


# Marcos
consumer_key = 'mUj3SW1ZO0mvuU7WaI1bMXnFs'
consumer_secret = X
access_token = '806834637200850944-ys6CZL9gnmVyWjPD2AjvakkGocGnH5l'
access_secret = X

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)