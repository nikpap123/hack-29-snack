import keras
import numpy as np
import imutils
from mrcnn.config import Config
from mrcnn import model as modellib
import os
import cv2

"""
#example usage:

person_model = load_rcnn_model()

img = cv2.imread("filename.jpg")

if detect_person(person_model, img):
    # invalid picture, blocked by person
    return None

else
    return <detect snacks>

"""



PERSON_MODEL = "mask_rcnn_coco.h5"

# load the mask_rcnn model for person detection
def load_rcnn_model(filename=PERSON_MODEL):
    config = SimpleConfig()
    # initialize the Mask R-CNN model for inference and then load the
    # weights
    print("[INFO] loading Mask R-CNN model...")
    mask_rcnn = modellib.MaskRCNN(mode="inference", config=config,
            model_dir=os.getcwd())
    mask_rcnn.load_weights(filename, by_name=True)
    return mask_rcnn

# return boolean if person found in image
def detect_person(mask_rcnn, img, confidence=0.7):
    image = imutils.resize(img, width=512)
    r = mask_rcnn.detect([image], verbose=0)[0]
    # people have class id 1
    p_person = r["scores"][np.argwhere(r["class_ids"] == 1)]
    return (p_person > confidence).size > 0
    

CLASS_NAMES = {i: i for i in range(81)}
class SimpleConfig(Config):
        # give the configuration a recognizable name
        NAME = "coco_inference"

        # set the number of GPUs to use along with the number of images
        # per GPU
        GPU_COUNT = 1
        IMAGES_PER_GPU = 1

        # number of classes (we would normally add +1 for the background
        # but the background class is *already* included in the class
        # names)
        NUM_CLASSES = len(CLASS_NAMES)

