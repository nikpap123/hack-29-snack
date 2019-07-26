from sklearn import svm
import numpy as np
from PIL import Image
import os
import glob
import re
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.externals import joblib

path = '/Users/xingyaoc/hack-29-snack/snack-photos/crop'

imfile_empty = glob.glob(os.path.join(path,'e*.jpg'))

imfile_full = glob.glob(os.path.join(path,'img*.jpg'))

labels_empty = [0]*len(imfile_empty)
labels_full = [1]*len(imfile_full)
labels = np.array(labels_empty + labels_full)


data = np.empty((len(labels), 43200))
for i, imfile in enumerate(imfile_empty+imfile_full):
    im = Image.open(imfile)
    data[i,:] = np.array(im).flatten()


X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.20, random_state=42)

tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                     'C': [1, 10, 100, 1000]},
                    {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]

scores = ['precision', 'recall']

for score in scores:
    print("# Tuning hyper-parameters for %s" % score)
    print()
    clf = GridSearchCV(SVC(), tuned_parameters, cv=5,
                       scoring='%s_macro' % score)
    clf.fit(X_train, y_train)

    print("Best parameters set found on development set:")
    print()
    print(clf.best_params_)
    print()
    print("Grid scores on development set:")
    print()
    means = clf.cv_results_['mean_test_score']
    stds = clf.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, clf.cv_results_['params']):
        print("%0.3f (+/-%0.03f) for %r"
              % (mean, std * 2, params))
    print()

    print("Detailed classification report:")
    print()
    print("The model is trained on the full development set.")
    print("The scores are computed on the full evaluation set.")
    print()
    y_true, y_pred = y_test, clf.predict(X_test)
    print(classification_report(y_true, y_pred))
    print()



best_clf = SVC(C=1.0, kernel='linear')
best_clf.fit(data, labels)
y_true, y_pred = y_test, clf.predict(X_test)
print(classification_report(y_true, y_pred))
joblib.dump(best_clf, 'snack_model_trained.pkl') 