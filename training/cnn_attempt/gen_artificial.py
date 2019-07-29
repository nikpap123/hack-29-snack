# Script to generate snack rack images by recombining images of empty and full trays
# Modified from Xingyao's crop function for manual labeling

from PIL import Image
import os
import glob
from collections import defaultdict

import numpy as np
import cv2
import random
import pandas as pd

import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--imgs", required=True,
        help="path to save the images and labels")
args = vars(ap.parse_args())

def crop_row(imfile, height, width, x, y, row, skip, padding):
    k = 0
    in_path = imfile
    im = Image.open(in_path)
    imgwidth, imgheight = im.size
    toReturn = []
    for j in range(x,imgwidth-padding,width+skip):
        box = (j, y, j+width, y+height)
        a = im.crop(box)
        toReturn.append((j, y, j+width, y+height, a))
        # top left coordinates, the cropped image
        k +=1

    return toReturn

empty_trays = []
imfile = "gen_data/all_empty0.jpg"
empty_trays += crop_row(imfile, 120, 120, 80, 0, 1, 0, 100)
empty_trays += crop_row(imfile, 150, 120, 100, 210, 2, 20, 100)
empty_trays += crop_row(imfile, 160, 120, 120, 380, 3, 10, 100)
empty_trays += crop_row(imfile, 180, 120, 110, 620, 4, 10, 100)


NEW_DATA = args["imgs"]
LABEL_DATA = NEW_DATA + "/labels.csv"
full_img = cv2.imread("gen_data/all_full.jpg")

SIZE = 120
labels = defaultdict(list)
for i in range(1):
    new_file = NEW_DATA + "random{}.jpg".format(i)
    bits = [random.randint(0,1) for b in range(21)]
    new_img = np.copy(full_img)
    for index, b in enumerate(bits):
        if b == 0:
            x, y, x_end, y_end, tray = empty_trays[index]
            new_img[y:y_end, x:x_end] = tray

    labels['filename'].append(new_file)
    labels['labels'].append(str(bits)[1:-1])
#    new_img = cv2.resize(new_img, (224,224))
    cv2.imwrite(new_file, new_img)
    #cv2.imshow("new", new_img)
    #cv2.waitKey(0)

pd.DataFrame(labels).to_csv(LABEL_DATA)
