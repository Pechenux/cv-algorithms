import cv2 as cv
from run_images import run_images

def HSV(input):
    return cv.cvtColor(input, cv.COLOR_BGR2HSV)

run_images(HSV)
