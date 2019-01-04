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
    # popularhashtags = ["pitti", "suitup", "suitandtie", "menwithclass", "tie", "gentleman", "suit", "menstyle", "wedding", "fashion", "dapper", "luzern", "zurich", "dandy"]
    # britman class tags
    # popularhashtags = ["mensclothing", "lucerne", "photooftheday", "lifestyle", "luxury", "blogger", "picoftheday", "vintage", "modamasculina"]
    # popularhashtags = ["lifestyle", "luxury", "switzerland", "blogger", "picoftheday", "vintage", "modamasculina"]
    # popularhashtags = ["zurich", "luzern", "ootd", "suit", "switzerland", "tie", "style", "gentleman", "fashion", "classy", "wedding", "suitup"]
    # most popular tags
    # unfollower = Unfollower()
    # unfollower.start()
    # unfollower.join()
    # popularhashtags = ["dandy", "switzerland", "suitup", "travel", "classy", "car", "zurich", "style", "luzern", "ootd", "instagood"]
    # popularhashtags = ["travel", "blogger", "picoftheday", "vintage", "modamasculina", "fashion", "luzern", "switzerland", "dapper", "wedding", "fashionpost", "lucerne", "fashionphotography", "gentleman", "suit", "tie", "pocketsquare", "ootd", "instagood"]
    popularhashtags = ["luzern", "switzerland", "dapper", "wedding", "fashionpost", "lucerne", "fashionphotography", "mensfashion", "gentleman", "suit", "tie", "pocketsquare", "ootd", "instagood"]
    for hashtag in popularhashtags:
        print('################################')
        print('## Starting Liker for Hashtag #' + hashtag)
        print('################################')
        hashtagLiker = HashtagLiker(hashtag)
        hashtagLiker.start()
        i = int(random.random()*946)
        time.sleep(i)
        hashtagLiker.stop()
        time.sleep(i*3)
    # likersliker = LikersLiker()
    # likersliker.start()
    # likersliker.join()

if __name__ == "__main__":
    main()
