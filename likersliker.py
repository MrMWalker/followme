import urllib
import ImageLoader
import dataLoader
import convNetColorNetwork
import time
import threading
import random
import settings

from classificationNetwork import ClassificationNetwork
from InstagramAPI import InstagramAPI
from tqdm import tqdm


class LikersLiker(threading.Thread):

    def __init__(self):
        super(LikersLiker, self).__init__()
        self._stop_event = threading.Event()

    def run(self):
        self.likeMenWithClassLikers()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


    def likeMenWithClassLikers(self):
        api = InstagramAPI(settings.USER_NAME, settings.USER_PW)
        next_max_id = None
        img_size = 200
        model_path = "models/LikeNotlike-3.model"
        model = convNetColorNetwork.create_model(img_size, 0.001)
        network = ClassificationNetwork(model, img_size, model_path)
        network.load_model()
        if api.login():
            print("Login succes!")

            api.getMediaLikers('1981826810129522964_4775415179')
            imageLikers = ImageLoader.getImageLikers(api.LastJson)
            user_count = 1
            for imageLiker in imageLikers[40:]:
                if user_count % 98 == 0:
                    time.sleep(int((random.random()+0.2)*100))
                if not imageLiker[1]:
                    self.likePicturesByUsername(api, imageLiker[0], network)
                    time.sleep(4)
                user_count = user_count + 1
                print(user_count)
            api.logout()

        else:
            print("Can't login!")
            return "Can't login!"

    def likePicturesByUsername(self, api, imageLiker_PK, network):
        like_count_by_user = 0
        img_path = "images/tmp/img.jpg"
        api.getUserFeed(imageLiker_PK)
        userImagesURLs = ImageLoader.getImageURLsByUsername(api.LastJson)
        for url in tqdm(userImagesURLs):
            urllib.request.urlretrieve(url[0], img_path)
            img = dataLoader.load_image(img_path, img_size=200)
            probability, str_label, label = network.predict(img)

            if str_label == "like":
                self.like(api, url)
                like_count_by_user = like_count_by_user + 1
                time.sleep(1.5)
                if like_count_by_user >= 2:
                    return
        #if like_count_by_user >= 4:
         #   api.follow(url[2])
          #  print("followed user" + str(url[2]))
           # with open('followed_users.txt', 'a') as outfile:
            #    outfile.write("\n" + str(url[2]))
             #   outfile.close()

    def like(self, api, url):
        api.like(url[1])
        with open('interacted_users.txt', 'a') as outfile:
            outfile.write("\n" + str(url[2]))
            outfile.close()
