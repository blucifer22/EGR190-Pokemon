import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
import h5py
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import PIL
from PIL import Image
os.environ['KMP_DUPLICATE_LIB_OK']='True'

PATH = os.getcwd()

def mylistdir(directory):
    """A specialized version of os.listdir() that ignores files that
    start with a leading period."""
    filelist = os.listdir(directory)
    return [x for x in filelist
            if not (x.startswith('.'))]

SIDE = 100
allImg = []
count = 0

for folder in mylistdir(PATH):
    if folder != "image_flatten.py":
        for img in mylistdir(os.path.join(PATH, folder)):
            if count < 10:
                #print(mylistdir(os.path.join(PATH, folder)))
                path = os.path.join(PATH, folder)
                print(img)
                img_array = cv2.imread(os.path.join(path, img))
                print(img_array)
                plt.imshow(img_array, cmap="gray")
                img_array = 1 - img_array/255.0
                img_array = cv2.resize(img_array, (SIDE, SIDE))
                plt.imshow(img_array, cmap="gray")
                allImg.append(img_array)
                plt.show()
                #results = model.predict(test_images)
                count += 1