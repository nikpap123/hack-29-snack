
from PIL import Image
import os
import glob
from crop import crop_row

path = '/Users/xingyaoc/hack-29-snack/snack-photos'
imgname = '2019-s-25_105729.jpg'


for i, imfile in enumerate(glob.glob(os.path.join(path,'empty*.jpg'))):
    print(imfile)
    crop_row(path, imfile, 120, 120, 80, 0, 1, 0, 100, i)
    crop_row(path, imfile, 120, 120, 100, 240, 2, 20, 100, i)
    crop_row(path, imfile, 120, 120, 120, 420, 3, 10, 100, i)
    crop_row(path, imfile, 120, 120, 110, 680, 4, 10, 100, i)