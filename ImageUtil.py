import cv2
from matplotlib import pyplot as plt


"""
    Read an image, and return its greyscale version
"""
def read_image(path):
    img = cv2.imread(path, 0)

    if img is None:
        raise Exception("The image path is incorrect")

    return img


"""
    Display the picture
"""
def display_image(img):
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])
    plt.show()


"""
    Save the picture in png
"""
def save_image(img, file_name):
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])
    plt.savefig("res/" + file_name)

