# Dependencies
import time
import tweepy

# Twitter API Keys
# Twitter API Keys
consumer_key = 'n1sAdlZkFmYtjQjnKi4tvWVvq'
consumer_secret = 'Whrb65sNFHQ4r1x7XbaumLuaioCQ5qMnmzRoBgqGRJkJTlAcc7'
access_token = '975007267899703296-EK68p5xrtfuwJcFSEobrPT7k6hLwlAn'
access_token_secret = 'uWuNHTj8GXHUUOdnKphHkyLdVyiE8tpXWQ5EPNxUa37PY'

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Loop through all tweets
tweet_num =1
while tweet_num <6 :
    api.update_status("tweet num " + str(time.ctime()) + "counter " + str(tweet_num))
    tweet_num  = tweet_num + 1
    time.sleep(60)