import os
from .crop import make_input_data
import numpy as np
from sklearn.svm import SVC
from sklearn.externals import joblib

def predict(imname):
    path = os.path.dirname(os.path.realpath(__file__))
    imfilepath = os.path.abspath(os.path.join(path, '..', imname))
    print(imfilepath)
    crop_data = make_input_data(imfilepath)
    data = np.empty((21, 43200))
    clf = joblib.load(os.path.join(path, 'snack_model_trained.pkl'))
    for i, im in enumerate(crop_data):
        data[i,:] = np.array(im).flatten()
    y_pred = clf.predict(data)
    return y_pred
