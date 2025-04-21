import cv2 as cv
from run_images import run_images

def Rotate45(input):
    width, height = input.shape[1::-1]
    center_of_image = (int(width / 2), int(height / 2))

    return cv.warpAffine(input, cv.getRotationMatrix2D(center_of_image, 45, 0.7), (width, height))

run_images(Rotate45)
