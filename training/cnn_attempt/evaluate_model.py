# Evaluates a model using keras
# use gen_artificial.py to generate the validation images as well?

import keras
import numpy as np
import imutils
from mrcnn.config import Config
from mrcnn import model as modellib
import os
import cv2
import csv

VALIDATION_LABELS = "validation/labels.csv"
MODEL = "mse_1000.h5"

# load the modified vgg model trained on our own data
def load_snack_model(filename):
    return keras.models.load_model(filename)

def load_training_data():
    train_images = []
    train_labels = []
    with open(VALIDATION_LABELS) as f:
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

snack = load_snack_model(MODEL)
v_imgs, v_lbls = load_training_data()
results = snack.evaluate(x=v_imgs, y=v_lbls)
