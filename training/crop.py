
from PIL import Image
import os
import glob

def crop_row(path, imfile, height, width, x, y, row, skip, padding, imnum):
    k = 0
    in_path = imfile
    im = Image.open(in_path)
    imgwidth, imgheight = im.size
    for j in range(x,imgwidth-padding,width+skip):
        box = (j, y, j+width, y+height)
        a = im.crop(box)
        a.save(os.path.join(path, 'crop', "img{}-row{}-{}.jpg".format(imnum, row, k)))
        k +=1