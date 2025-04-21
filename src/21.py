import cv2 as cv
from run_images import run_images

def Blur(input):
    return cv.GaussianBlur(input, (31, 31), 0)

run_images(Blur)
