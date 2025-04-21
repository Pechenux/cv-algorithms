import cv2 as cv
import numpy as np
from run_images import run_images

def Gamma(input):
    invGamma = 1.0 / 1.35
    table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")

    return cv.LUT(input, table)

run_images(Gamma)
