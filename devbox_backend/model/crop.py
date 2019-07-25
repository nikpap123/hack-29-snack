
from PIL import Image
import os
import glob

def crop_row(im, height, width, x, y, row, skip, padding):
    row_data = []
    imgwidth, imgheight = im.size
    for j in range(x,imgwidth-padding,width+skip):
        box = (j, y, j+width, y+height)
        a = im.crop(box)
        row_data.append(a)
    return row_data

def make_input_data(imfile):
    crop_data = []
    in_path = imfile
    im = Image.open(in_path)
    crop_data += crop_row(im, 120, 120, 80, 0, 1, 0, 100)
    crop_data += crop_row(im, 120, 120, 100, 240, 2, 20, 100)
    crop_data += crop_row(im, 120, 120, 120, 420, 3, 10, 100)
    crop_data += crop_row(im, 120, 120, 110, 680, 4, 10, 100)
    return crop_data
