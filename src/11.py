import cv2 as cv
from run_images import run_images

def Brightness(input):
    return cv.convertScaleAbs(input, beta=100)

run_images(Brightness)
