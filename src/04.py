import cv2 as cv
from run_images import run_images

def GrayScale(input):
    return cv.cvtColor(input, cv.COLOR_BGR2GRAY)

run_images(GrayScale)
