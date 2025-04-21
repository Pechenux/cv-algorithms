import cv2 as cv
import numpy as np
from run_images import run_images

x_point_percent = 70
y_point_percent = 10

def TenPixelsRight(input):
    return cv.warpAffine(input, np.float32([[1, 0, 10], [0, 1, 0]]), (input.shape[1::-1]))

run_images(TenPixelsRight)
