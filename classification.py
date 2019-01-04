import argparse
from datetime import datetime
import convNetColorNetwork
import dataLoader
from classificationNetwork import ClassificationNetwork


def main():
    default_model_path = "models/Inception/acneRecognizer-0.001-inception-GPU-Run-Quantil1_Final.model"
    parser = argparse.ArgumentParser(description='Classify image')
    parser.add_argument('--model_path', type=str, default=default_model_path,
                        help='The directory where the saved model is found')
    parser.add_argument('--img_path', type=str, help='The input image')
    arguments = parser.parse_args()

    if arguments.img_path is None:
        print('Please provide --img_path option.')
        return

    apply_classification(arguments.model_path, arguments.img_path)


def apply_classification(model_path: str, img_path: str):
    print("{}: Load image...".format(datetime.now()))
    img_size = 200
    img = dataLoader.load_image(img_path, img_size)

    print("{}: Calculate prediction...".format(datetime.now()))
    model = convNetColorNetwork.create_model(img_size,0.001)
    network = ClassificationNetwork(model, img_size, model_path)
    network.load_model()

    probability, str_label, label = network.predict(img)
    print("{0}: Prediction: {1}, Probability: {2:.5f}".format(datetime.now(), str_label, probability))


if __name__ == "__main__":
    main()
