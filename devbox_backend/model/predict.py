
from PIL import Image
import os
import glob
from crop import make_input_data
import numpy as np
from sklearn.svm import SVC
from sklearn.externals import joblib
from joblib import dump, load


path = '/Users/xingyaoc/hack-29-snack/devbox_backend/model'
imname = 'empty_rm2.jpg'

def predict(path, imname):
    imfilepath = os.path.join(path, imname)
    crop_data = make_input_data(path, imfilepath)
    data = np.empty((21, 43200))
    clf = joblib.load('snack_model_trained.pkl')
    for i, im in enumerate(crop_data):
        data[i,:] = np.array(im).flatten()
    y_pred = clf.predict(data)
    return y_pred

print(predict(path, imname))
