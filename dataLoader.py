import os
from random import shuffle

import numpy as np
from cv2 import cv2

from tqdm import tqdm

def load_data(data_dir: str,img_size: int):
    like_data = __load_data(data_dir, "like", img_size, grayscale=False)
    notlike_data = __load_data(data_dir, "notlike", img_size, grayscale=False)
    like_data.extend(notlike_data)
    return like_data

def flip_image(img):
    return cv2.flip(img, 1)


def load_image(img_path: str, img_size: int, grayscale=False):
    if grayscale:
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    else:
        img = cv2.imread(img_path, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (img_size, img_size))
    return img


def __get_label(str_label):
    if str_label == "like":
        return [1, 0]
    return [0, 1]


def __load_data(dir, str_label, img_size: int, grayscale=False):
    data = []
    train_path = os.path.join(dir, str_label)
    for img_name in tqdm(os.listdir(train_path)):
        img_path = os.path.join(dir, str_label, img_name)
        img = load_image(img_path, img_size, grayscale)
        label = __get_label(str_label)
        data.append([np.array(img), np.array(label)])
    return data


def load_test_data(test_dir, img_size: int, grayscale=False):
    test_data = []
    acne = __load_data(test_dir, "acne", img_size, grayscale)
    no_acne = __load_data(test_dir, "noacne", img_size, grayscale)
    test_data.extend(acne)
    test_data.extend(no_acne)
    shuffle(test_data)
    return test_data
