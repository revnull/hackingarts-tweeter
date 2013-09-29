#!/usr/bin/env python
'''
Class for searching a twitter hashtag and returning tweets in tokenized form
'''

import twitter
import os
import sys
from re import sub, split

 
class Reader():
    '''
    Performs functions associated with reading the twitter feed and providing
    parsed and tokenized output.
    
    tweets(hashtag)
    words(tweet)
    '''
 
    def __init__(self, app_name, consumer_key, consumer_secret):
        creds = os.path.expanduser('~/.tweeter_credentials')
        if not os.path.exists(creds):
            twitter.oauth_dance(
                                app_name, consumer_key, consumer_secret,
                                creds)
        oauth_token, oauth_secret = twitter.read_token_file(creds)
        self.t = twitter.Twitter(
                                 auth=twitter.OAuth(
                                                    oauth_token, oauth_secret,
                                                    consumer_key, consumer_secret
                                                    )
                                 )
 
    def tweets(self, hashtag):
        '''
        Return a list of all of the tweets (strings) matching the hashtag.
        Specify the hashtag without the "#" character.
        '''
        hashtag = sub(r'^#', '', hashtag)
        o = self.t.search.tweets(q='#'+hashtag, count=8)
        stats = o.get('statuses')
        tweets = [s['text'] for s in stats]
        return tweets
    
    def words(self, tweet):
        '''
        Given a tweet (string), return a list of "words".
        For now, this is just a list of strings split on whitespace. 
        '''
        words = split(r'\s+', tweet)
        return words

    def all_words(self, hashtag):
        '''
        Returns a list of all of the words for the given hashtag.
        TODO:  have parameters for specifying a timestamp search range. 
        '''
        res = []
        for tweet in self.tweets(hashtag):
            res +=  self.words(tweet)
        return res
    

def main(argv):
    r = Reader(argv[0], argv[1], argv[2])
    print "\n".join(r.all_words('ackingarts'))
    
if __name__ == '__main__':
    main(sys.argv[1:])
