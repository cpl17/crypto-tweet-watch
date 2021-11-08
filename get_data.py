from slistener import MyStreamListener

import os
from dotenv import load_dotenv


# Load and Store Tokens 

load_dotenv()

consumer_key = os.getenv("APIKEY")
consumer_secret = os.getenv("APISECRET")
access_token = os.getenv("ACCESSTOKEN")
access_token_secret = os.getenv("ACCESSSECRET")

if __name__ == "__main__":

    stream = MyStreamListener(consumer_key,consumer_secret,access_token,access_token_secret,fprefix='crypto')

    print("Streaming started...")

    stream.filter(track = ['crypto'],languages=['en'])
