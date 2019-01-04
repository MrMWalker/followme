import urllib
import ImageLoader
import dataLoader
import convNetColorNetwork
import time
import threading
import settings

from classificationNetwork import ClassificationNetwork
from InstagramAPI import InstagramAPI
from tqdm import tqdm

api = InstagramAPI(settings.USER_NAME, settings.USER_PW)

if api.login():
    print("Login succes!")

else:
    print("Can't login!")

api.getSelfUserFeed()
json = api.LastJson
print("end")

# pk menwithclass 208101486

api.getUserFeed('208101486')
json = api.LastJson
print("end")

#image with many likes 1829875825206494802
api.getMediaLikers('1829875825206494802')
json = api.LastJson
print('end')