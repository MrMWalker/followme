#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
import time
import random
import settings


from bulkUnfollow import Unfollower
from hashtagliker import HashtagLiker
from likersliker import LikersLiker

def main():
    # popularhashtags = ["gentleman", "suit", "style", "wedding", "fashion", "luzern", "tie", "ootd", "dapper", "zurich", "lucerne", "dandy", "suitandtie", "classy", "pocketsquare"]
    # popularhashtags = ["classy", "suitup", "suitandtie", "menwithclass", "tie", "gentleman", "suit", "menstyle", "wedding", "fashion", "dapper", "luzern", "zurich", "dandy"]
    # britman class tags

    # city hashtags
    # popularhashtags = ["luzern", "zurich", "bern", "basel", "newyork", "london", "lucerne", "schweiz", "manchester"]
    # popularhashtags = ["mensclothing", "lucerne", "photooftheday", "lifestyle", "luxury", "blogger", "picoftheday", "vintage", "modamasculina"]
    # popularhashtags = ["lifestyle", "luxury", "switzerland", "blogger", "picoftheday", "vintage", "modamasculina"]
    popularhashtags = ["zurich", "luzern", "spezzatura", "ootd", "suit", "switzerland", "tie", "style", "gentleman", "fashion", "lucerne", "classy", "wedding", "suitup"]
    # most popular tags
    # unfollower = Unfollower()
    # unfollower.start()
    # unfollower.join()
    # popularhashtags = ["follow4follow", "luzern", "dandy", "switzerland", "suitup", "travel", "classy", "car", "zurich", "style", "lucerne", "ootd", "instagood"]
    # popularhashtags = ["fashionpost", "lucerne", "fashionphotography", "gentleman", "suit", "tie", "pocketsquare", "ootd", "mentrend", "luzern"]
    # popularhashtags = ["fashionphotography", "dapperdandy", "mensfashion", "gentleman", "suit", "tie", "pocketsquare", "ootd", "instagood", "classydapper"]
    # popularhashtags = ["travel", "gentlemanlike", "suitandtie", "pittiuomo", "vintage", "modamasculina", "suitup", "lucerne", "zurich"]
    # popularhashtags = ["floralprint", "dapper", "dandy", "wedding", "lucerne"]
    # popularhashtags = ["luzern", "schweiz", "zurich", "stuttgart", "paris"]


    for hashtag in popularhashtags:
        print('################################')
        print('## Starting Liker for Hashtag #' + hashtag)
        print('################################')
        hashtagLiker = HashtagLiker(hashtag)
        hashtagLiker.start()
        i = int(random.random()*846)
        time.sleep(i)
        hashtagLiker.stop()
        time.sleep(i*1.5)

    # likersliker = LikersLiker()
    # likersliker.start()
    # likersliker.join()

if __name__ == "__main__":
    main()
