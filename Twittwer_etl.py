import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs

def run_twitter_etl():

    API_KEY = "ZcV2PUP3FUoR99eLjwWVLBrxZ"

    API_KEY_SECRET = "DRKKOykeyeeR1b7an9P8wMXpPxd8N4KiqecZkXYOpjzF6wwS1n"

    Access_Token = "1604137373171798017-eiz1fflRU4yufrzeR3KgyPgW1mn0jB"

    Access_Token_Secret = "j4y0wMcli0wgR3nYfhitDIXEBFPRz5Ts4kCQ4keD5xmMw"

    #TWITTER AUTHENTICATION

    auth =tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(Access_Token, Access_Token_Secret)

    #creating an API object

    api=tweepy.API(auth)

    tweets = api.user_timeline(screen_name = '@elonmusk',
                            
                                count = 20,
                                include_rts = False,
                                tweet_mode ='extentded'
                            )
    list = []
    for tweet in tweets:
         text = tweet._json["full_text"]

        refined_tweet = {"user": tweet.user.screen_name,
                            'text' : text,
                            'favorite_count' : tweet.favorite_count,
                            'retweet_count' : tweet.retweet_count,
                            'created_at' : tweet.created_at}
            
    list.append(refined_tweet)

    df = pd.DataFrame(list)
    df.to_csv('refined_tweets.csv')
