#!/usr/bin/python
import time
import os
from TwitterSearch import *
from threading import Thread

def Tweety():    
    try:
        Twitter_User = TwitterUserOrder('EmreOvunc')        
        Twitter_Obj = TwitterSearch(
            consumer_key = 'XX',
            consumer_secret = 'XX',
            access_token = 'XX',
            access_token_secret = 'XX'
         )
        for tweet in Twitter_Obj.search_tweets_iterable(Twitter_User):
            tweets=( '@%s : %s \n' % (tweet['user']['screen_name'], tweet['text']) )
            
            # You can use if statement for spesific tweets
            # or skip this part to save all tweets
            if '#TweetyBot' in tweets:
                if CheckTweets(tweets[13:])== 1:                
               		break;
    except TwitterSearchException as error:
        print(error)
        
def CheckTweets(Tweet):
   # Tweet=Tweet.replace("#TweetyBot ","")
    TweetFile= open("/home/debian/Desktop/Last_Tweet.txt", "r")
    LastTweet=TweetFile.read()
    if LastTweet.encode("utf-8").split() == Tweet.encode("utf-8").split():
        TweetFile.close()
        return 1
    else:
        TweetFile.close()
        os.remove("/home/debian/Desktop/Last_Tweet.txt")
        TweetFile= open("/home/debian/Desktop/Last_Tweet.txt", "w")
        TweetFile.write(Tweet)
        TweetFile.close()
        return 1

def TimeFunc():
	Tweety()
	time.sleep(120)
	return TimeFunc()


TimeFunc()
