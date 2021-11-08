from tweepy import Stream
import json
import time
import sys
import os


class MyStreamListener(Stream):

    def __init__(self,consumer_key, consumer_secret,access_token,access_token_secret, fprefix = 'streamer'):

        super().__init__(consumer_key, consumer_secret,access_token,access_token_secret)

        self.counter = 0
        self.num_json = 0
        self.fprefix = fprefix
        self.output  = open('%s_%s.json' % (self.fprefix, time.strftime('%Y%m%d-%H%M%S')), 'w')
        
        

    #Write Tweet to Json
    def on_status(self, status):
        
        status_str = json.dumps(status._json)
        self.counter += 1
        if self.counter == 1:
            self.output.write("[" + status_str)
        elif self.counter <10000:
            self.output.write("," + status_str)
        if self.counter >= 10000:
            self.output.write("," + status_str + "]")
            self.output.close()
            self.counter = 0

            if self.num_json <4:
                self.output  = open('%s_%s.json' % (self.fprefix, time.strftime('%Y%m%d-%H%M%S')), 'w')
                self.num_json += 1
            else:
                self.disconnect()
        return


    def on_delete(self, status_id, user_id):
        print(f"Delete notice for user {user_id} on tweet {status_id}")
        return


    def on_limit(self, track):
        print(f"WARNING: Limitation notice received, tweets missed: {track}")
        return


    def on_error(self, status_code):
        print('Encountered error with status code:', status_code)
        return 


    def on_timeout(self):
        print("Timeout, sleeping for 60 seconds...")
        time.sleep(60)
        return