import cv2 as cv
from run_images import run_images

def VertacalMirror(input):
    return cv.flip(input, flipCode=1)

run_images(VertacalMirror)
