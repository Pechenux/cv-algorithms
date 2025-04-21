import cv2 as cv
import numpy as np
from run_images import run_images

def Sobel(input):
    gray = cv.cvtColor(input, cv.COLOR_BGR2GRAY)
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    sobel = cv.filter2D(gray, -1, kernel)
    return sobel

run_images(Sobel)
