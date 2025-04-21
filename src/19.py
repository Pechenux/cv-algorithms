import cv2 as cv
import numpy as np
from run_images import run_images

def Contours(input):
    thr = cv.threshold(input, 128, 255, 0)[1]

    cntr = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[0]

    img = np.ones(input.shape, dtype=np.uint8) * 255
    cv.drawContours(img, cntr, -1, (0, 255, 0), 1)

    return img

run_images(Contours, cv.IMREAD_GRAYSCALE)
