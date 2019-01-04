import tflearn

from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression

import dataLoader
from classificationNetwork import ClassificationNetwork

IMG_SIZE = 200

def create_model(img_size: int, lr=1e-3):
    # 6 Convolutional Layers
    convnet = input_data(shape=[None, img_size, img_size, 3], name="input")

    convnet = conv_2d(convnet, 32, 2, activation="relu")  # 100x100x32
    convnet = max_pool_2d(convnet, 2)

    convnet = conv_2d(convnet, 64, 2, activation="relu")  # 50x50x64
    convnet = max_pool_2d(convnet, 2)

    convnet = conv_2d(convnet, 32, 2, activation="relu")  # 25x25x32
    convnet = max_pool_2d(convnet, 2)

    convnet = conv_2d(convnet, 64, 2, activation="relu")  # 13x13x64
    convnet = max_pool_2d(convnet, 2)

    convnet = conv_2d(convnet, 32, 2, activation="relu")  # 7x7x32
    convnet = max_pool_2d(convnet, 2)

    convnet = conv_2d(convnet, 64, 2, activation="relu")  # 4x4x65
    convnet = max_pool_2d(convnet, 2)

    convnet = fully_connected(convnet, 1024, activation="relu")
    convnet = dropout(convnet, 0.6)

    convnet = fully_connected(convnet, 2, activation="softmax")
    convnet = regression(convnet, optimizer="adam", learning_rate=lr,
                         loss="categorical_crossentropy", name="targets")

    model = tflearn.DNN(convnet, tensorboard_dir="log")
    return model

def main():
    train_dir = "images/train"
    test_dir = "images/test"
    lr = 1e-3  # learning rate 0.001
    IMG_SIZE = 200

    experiment_no = "1"
    model_name = "LikeNotlike-{}.model".format(experiment_no)
    model_path = "models/" + model_name

    train_data = dataLoader.load_data(train_dir, IMG_SIZE)
    test_data = dataLoader.load_data(test_dir, IMG_SIZE)
    model = create_model(IMG_SIZE, lr)
    network = ClassificationNetwork(model, IMG_SIZE, model_path)
    network.fit_model(train_data, test_data)

if __name__ == "__main__":
    main()
