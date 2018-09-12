import tweepy
 
# Consumer keys and access tokens, used for OAuth
consumer_key = ‘XXXXXXXXXXXXX’
consumer_secret = ‘XXXXXXXXXXXXX’
access_token = ‘XXXXXXXXXXXXX’
access_token_secret = ‘XXXXXXXXXXXXX’
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
 
# Sample method, used to update a status, you can write message whatever you want to post in twitter
api.update_status(‘Happy Coding!' + " #LearnPython")
