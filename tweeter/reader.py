#!/usr/bin/env python
'''
Class for searching a twitter hashtag and returning tweets in tokenized form
'''

import twitter
import os
import sys
from re import sub

 
class Reader():
 
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
        '''Return a list of all of the tweets matching the hashtag'''
        hashtag = sub(r'^#', '', hashtag)
        o = self.t.search.tweets(q='#'+hashtag)
        stats = o.get('statuses')
        tweets = [s['text'] for s in stats]
        return tweets
    
def main(argv):
    r = Reader(argv[0], argv[1], argv[2])
    print "\n".join(r.tweets('ackingarts'))
    
    
if __name__ == '__main__':
    main(sys.argv[1:])
