#modified from
#https://www.pyimagesearch.com/2019/06/10/keras-mask-r-cnn/

import keras
import numpy as np
from keras.applications import vgg16
from keras.models import Model
from keras.layers import Dense

import argparse
import cv2
import csv

def load_training_data():
    train_images = []
    train_labels = []
    with open(args["labels"]) as f:
        csv_reader = csv.reader(f, delimiter=',')
        next(csv_reader) # ignore header
        for row in csv_reader:
            img_name = row[1]
            label = [int(a) for a in row[2].split(",")]
            img_raw = cv2.imread(img_name)
            img = cv2.resize(img_raw, (224,224))

            train_images.append(img)
            train_labels.append(label)

    return np.array(train_images), np.array(train_labels)

test_img = np.array([cv2.resize(cv2.imread("full.jpg"), (224,224))])

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-l", "--labels", required=True,
	help="path to labels file")
ap.add_argument("-m", "--model", required=True,
	help="path to save the resulting model")
args = vars(ap.parse_args())

vgg_model = vgg16.VGG16(weights='imagenet')

snack_layer = Dense(21, activation='sigmoid', trainable=True)(vgg_model.layers[-2].output)
for l in vgg_model.layers[:-3]:
    l.trainable = False

snack_model = Model(input=vgg_model.inputs, output=snack_layer)

train_images, train_labels = load_training_data()
print("Loaded training data")

before_train = snack_model.predict(test_img)

snack_model.compile(optimizer="sgd", loss="mean_squared_error", metrics=['accuracy'])
print("Beginning training...")

hist = snack_model.fit(x=train_images, y=train_labels, epochs=3) #validation_split = 0.1 ?
print(hist.history)

snack_model.save(args["model"])
print("Saved new model to {}".format(args["model"]))

print("Before")
print(before_train)
print("After")
print(snack_model.predict(test_img))
