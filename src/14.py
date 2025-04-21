import cv2 as cv
import numpy as np
from run_images import run_images

def Hist(input):
    channels = cv.split(input)
    equalized_channels = [cv.equalizeHist(channel) for channel in channels]
    result = cv.merge(equalized_channels)

    gray_img = cv.cvtColor(input, cv.COLOR_BGR2GRAY)
    result_gray = cv.equalizeHist(gray_img)

    return [result, result_gray]

run_images(Hist)
