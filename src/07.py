import cv2 as cv
from run_images import run_images

def HorizontalMirror(input):
    return cv.flip(input, flipCode=0)

run_images(HorizontalMirror)
