import cv2 as cv
from run_images import run_images

def Binary(input):
    return cv.threshold(input, 128, 255, 0)[1]

run_images(Binary, cv.IMREAD_GRAYSCALE)
