#!/usr/bin/python

from TwitterAPI import TwitterAPI
import time

consumer_key = "xo6DT4E0SoZ1X3xLjKCw"
consumer_secret = "7gfkyjGXOmKFAJhjWs4aXnr9PYh2pHwkcNM6DNYBUhU"
access_token_key = "260744596-ewqESN55tyRocAYEsASwmPWUdnM2KoCkzlXyKcQz"
access_token_secret = "uHDubHtbt2TBSYjTnFvbEgNHGQ6AHNFlcEgDlxGp9E43N"

def main():

    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

    filter = ""

#get filter tag
    filter = "hey"

    r = api.request('statuses/filter', {"track": filter})    

    i = 0


    for item in r.get_iterator():
        i += 1
        time.sleep(1)
        print item
        if i == 5:
            break
    

if __name__== '__main__':
    main()
