import classification
import urllib
import ImageLoader
import dataLoader
import convNetColorNetwork
import time
import settings

from classificationNetwork import ClassificationNetwork
from InstagramAPI import InstagramAPI
from tqdm import tqdm


class ImageLiker:

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
            urllib.request.urlretrieve(url[0], img_path)
            img = dataLoader.load_image(img_path, img_size)
            # tqdm.write("{}: Calculate prediction...".format(datetime.now()))
            probability, str_label, label = network.predict(img)
            # tqdm.write("{0}: Prediction: {1}, Probability: {2:.5f}".format(datetime.now(), str_label, probability))

            if str_label == "like":
                api.like(url[1])
                time.sleep(2.5)
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
            while True:
                next_max_id = self.imgliker.likeBatchImagesByHashtag(self, hashtag, next_max_id, api, network)

        else:
            print("Can't login!")
            return "Can't login!"