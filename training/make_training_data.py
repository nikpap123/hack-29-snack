
from PIL import Image
import os
import glob
from crop import crop_row
import cv2
import numpy as np
path = '/Users/xingyaoc/hack-29-snack/snack-photos'
imgname = '2019-s-25_105729.jpg'


def normalization(img):
    for i in range(3):
       img[:,:,i]=np.absolute((img[:,:,i]-np.min(img[:,:,i]))/(np.max(img[:,:,i])-np.min(img[:,:,i])))*255
    return img

k = 35
for i, imfile in enumerate(glob.glob(os.path.join(path,'all_full.jpg'))):
    print(imfile)
    crop_row(path, imfile, 120, 120, 80, 0, 1, 0, 100, i+6, k)
    k+=6
    crop_row(path, imfile, 120, 120, 100, 240, 2, 20, 100, i+6, k)
    k+=5
    crop_row(path, imfile, 120, 120, 120, 420, 3, 10, 100, i+6,  k)
    k+=5
    crop_row(path, imfile, 120, 120, 110, 680, 4, 10, 100, i+6, k)
    k+=5