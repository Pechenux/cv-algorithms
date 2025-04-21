import cv2 as cv
from run_images import run_images

x_point_percent = 70
y_point_percent = 10

def Rotate30(input):
    width, height = input.shape[1::-1]
    point = (int(width * (x_point_percent / 100)), int(height * (y_point_percent / 30)))

    return cv.warpAffine(input, cv.getRotationMatrix2D(point, 30, 0.7), (width, height))

run_images(Rotate30)
