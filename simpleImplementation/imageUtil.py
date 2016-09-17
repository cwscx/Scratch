import cv2
import numpy as np


"""
    Read an image, and return its greyscale version
"""
def read_image(path):
    img = cv2.imread(path, 0)

    if img is None:
        raise Exception("The image path is incorrect")

    return img


"""
    Display the picture, should only be used for test
"""
def display_image(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()