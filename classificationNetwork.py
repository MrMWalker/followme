import os
from datetime import datetime

from tflearn import DNN
import numpy as np
import likePrediction


class ClassificationNetwork:
    def __init__(self, model: DNN, img_size: int, model_path: str):
        self.model = model
        self.model_path = model_path
        self.img_size = img_size

    def load_model(self):
        if os.path.exists("{}.meta".format(self.model_path)):
            self.model.load(self.model_path, weights_only=True)
            print("{}: Model loaded on path '{}'.".format(datetime.now(), self.model_path))
            return self.model
        else:
            raise FileNotFoundError("Model not found on path '{}'!".format(self.model_path))

    def fit_model(self, train_data: np.ndarray, test_data: np.ndarray, n_epoch=50, batch_size=100):
        train_X = np.array([i[0] for i in train_data])\
            .reshape(-1, self.img_size, self.img_size, 3)
        train_Y = [i[1] for i in train_data]

        test_x = np.array([i[0] for i in test_data])\
            .reshape(-1, self.img_size, self.img_size, 3)
        test_y = [i[1] for i in test_data]

        self.model.fit(train_X, train_Y, n_epoch=n_epoch, validation_set=(test_x, test_y),
                       shuffle=True, show_metric=True, batch_size=batch_size,
                       snapshot_step=300, run_id=self.model_path)

        self.model.save(self.model_path)

        return self.model

    def predict(self, img, ):
        return likePrediction.predict(self.model, img, self.img_size)

    def score(self, test_data):
        return likePrediction.score(self.model, test_data, self.img_size)