import numpy as np
import matplotlib.pyplot as plt
from tflearn import DNN


def predict(model: DNN, img: np.ndarray, img_size: int):
    # like: [1,0]
    # notlike: [0,1]
    data = img.reshape(img_size, img_size, 3)
    model_out = model.predict([data])[0]

    probability = np.max(model_out)
    if np.argmax(model_out) == 1:
        str_label = "notlike"
        label = [0, 1]
    else:
        str_label = "like"
        label = [1, 0]

    return probability, str_label, label


def score(model: DNN, test_data: np.ndarray, img_size: int):
    total = 0
    correct = 0
    for test_element in test_data:
        img = test_element[0]
        label = test_element[1]
        _, actual_label = predict(model, img, img_size)
        if (label == actual_label).all():
            correct += 1
        total += 1

    accuracy = correct / total
    print("Total: {}, Correct: {}, Accuracy: {}".format(total, correct, accuracy))
    return accuracy


def visualize_test(model: DNN, test_data: np.ndarray, img_size: int):
    fig = plt.figure()

    for num, test_element in enumerate(test_data[:12]):
        img = test_element[0]
        str_label, label = predict(model, img, img_size)
        y = fig.add_subplot(3, 4, num + 1)
        y.imshow(img, cmap="gray")
        plt.title(str_label)
        y.xaxis.set_visible(False)
        y.yaxis.set_visible(False)
    plt.show()
