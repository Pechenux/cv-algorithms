import cv2 as cv
from run_images import run_images

def CannyEdges(input):
    return cv.Canny(input, 75, 125)
    # return cv.Canny(input, 200, 400)  # best for 3

run_images(CannyEdges, cv.IMREAD_GRAYSCALE)
