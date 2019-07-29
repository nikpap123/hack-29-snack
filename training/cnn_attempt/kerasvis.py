# For introspection on the cnn trained from the generated data
# Generates the class activation maps for each of the 21 labels for each tray
# Warmer colors indicate the pixel is more important for that label
# Looks cool.

import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from vis.visualization import visualize_cam, overlay
from vis.utils import utils

import cv2
import model_interface as mi

img1 = cv2.resize(cv2.imread("offset.jpg"),(224,224))
model = mi.load_snack_model("binary_cross_entropy_1000.h5")
layer_idx = utils.find_layer_idx(model, 'dense_1')

for modifier in [None]:
    plt.figure()
    for i in range(21):    
        # 20 is the imagenet index corresponding to `ouzel`
        grads = visualize_cam(model, layer_idx, filter_indices=[i], 
                              seed_input=img1, backprop_modifier=modifier)        
        # Lets overlay the heatmap onto original image.    
        jet_heatmap = np.uint8(cm.jet(grads)[..., :3] * 255)
        plt.imshow(overlay(jet_heatmap, img1))
        plt.title(i)
        plt.show()
