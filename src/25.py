import cv2 as cv
import numpy as np
from run_images import run_images

def Dilate(input):
    kernel = np.ones((11, 11))

    return cv.dilate(input, kernel, iterations=1)

run_images(Dilate)
