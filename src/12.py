import cv2 as cv
from run_images import run_images

def Contrast(input):
    return cv.convertScaleAbs(input, alpha=1.6)

run_images(Contrast)
