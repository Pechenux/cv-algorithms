import cv2 as cv
import numpy as np
from run_images import run_images

def Laplacian(input):
    gray = cv.cvtColor(input, cv.COLOR_BGR2GRAY)
    kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    laplacian = cv.filter2D(gray, -1, kernel)
    return laplacian

run_images(Laplacian)
