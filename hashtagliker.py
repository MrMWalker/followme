import urllib
import ImageLoader
import dataLoader
import convNetColorNetwork
import time
import threading
import settings
import cfg

from classificationNetwork import ClassificationNetwork
from InstagramAPI import InstagramAPI
from tqdm import tqdm


class HashtagLiker(threading.Thread):

    def __init__(self,hashtag:str):
        super(HashtagLiker, self).__init__()
        self.hashtag = hashtag
        self._stop_event = threading.Event()

    def run(self):
        self.likeImagesByHashtag(self.hashtag)

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def likeBatchImagesByHashtag(self, hashtag: str, next_max_id: str, api, network):
        img_size = 200
        if (next_max_id == None):
            api.getHashtagFeed(hashtag)
        else:
            print("getting images with next_max_id:" + next_max_id)
            api.getHashtagFeed(hashtag,next_max_id)
        imgURLs = ImageLoader.getImageURLs(api.LastJson)
        # get next max ID
        next_max_id = ImageLoader.getNextMaxID(api.LastJson)
        img_path = "images/tmp/img.jpg"

        # calculate like probability per image
        for url in tqdm(imgURLs):
            # print(url[0])
            try:
                urllib.request.urlretrieve(url[0], img_path)
            except:
                print("loading of image failed")
            img = dataLoader.load_image(img_path, img_size)
            # tqdm.write("{}: Calculate prediction...".format(datetime.now()))
            probability, str_label, label = network.predict(img)
            # tqdm.write("{0}: Prediction: {1}, Probability: {2:.5f}".format(datetime.now(), str_label, probability))

            if str_label == "like":
                api.like(url[1])
                time.sleep(2.5)
                if cfg.mode == 2:
                    self.likePicturesByUsername(api, url, network)
                elif cfg.mode == 3:
                    self.likeLikersPictures(api,url,network)


        return next_max_id

    def likeImagesByHashtag(self, hashtag: str):
        api = InstagramAPI(settings.USER_NAME, settings.USER_PW)
        next_max_id = None
        img_size = 200
        model_path = "models/LikeNotlike-3.model"
        model = convNetColorNetwork.create_model(img_size, 0.001)
        network = ClassificationNetwork(model, img_size, model_path)
        network.load_model()
        if api.login():
            print("Login succes!")
            while not self.stopped():
                next_max_id = self.likeBatchImagesByHashtag(hashtag, next_max_id, api, network)
            api.logout()

        else:
            print("Can't login!")
            return "Can't login!"

    def likePicturesByUsername(self, api, url, network):
        like_count_by_user = 0
        img_path = "images/tmp/img.jpg"
        api.getUserFeed(url[2])
        userImagesURLs = ImageLoader.getImageURLsByUsername(api.LastJson)
        for url in tqdm(userImagesURLs):
            urllib.request.urlretrieve(url[0], img_path)
            img = dataLoader.load_image(img_path, img_size=200)
            probability, str_label, label = network.predict(img)

            if str_label == "like":
                api.like(url[1])
                like_count_by_user = like_count_by_user + 1
                time.sleep(3.2)
        if like_count_by_user >= 4:
            api.follow(url[2])
            print("followed user" + str(url[2]))
            with open('followed_users.txt', 'a') as outfile:
                outfile.write("\n" + str(url[2]))
                outfile.close()

    def likeLikersPictures(self, api, url, network):
        likers_count = 1
        img_path = "images/tmp/img.jpg"
        api.getMediaLikers(url[1])
        imageLikers = ImageLoader.getImageLikers(api.LastJson)
        for liker in imageLikers:
            if likers_count % 7  == 0:
                return
            elif not liker[1]: #check if account is private
                if not liker[0] == 321882169: #check if it is my account
                    self.likeLikersPicture(api, liker[0], network)
                    time.sleep(2)
            likers_count = likers_count + 1

    def likeLikersPicture(self, api, userId, network):
        img_path = "images/tmp/img.jpg"
        api.getUserFeed(userId)
        userImagesURLs = ImageLoader.getImageURLsByUsername(api.LastJson)
        count_likes = 0
        for url in tqdm(userImagesURLs):
            urllib.request.urlretrieve(url[0], img_path)
            img = dataLoader.load_image(img_path, img_size=200)
            probability, str_label, label = network.predict(img)

            if str_label == "like":
                api.like(url[1])
                time.sleep(2)
                count_likes = count_likes + 1
                if count_likes >= 2:
                    return
