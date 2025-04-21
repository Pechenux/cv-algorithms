import cv2 as cv
import numpy as np
from run_images import run_images

def Contours(input):
    gray = cv.cvtColor(input, cv.COLOR_BGR2GRAY)
    thr = cv.threshold(gray, 128, 255, 0)[1]
    cntr = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[0]

    return cv.drawContours(input.copy(), cntr, -1, (255, 0, 0), 1)

run_images(Contours)
