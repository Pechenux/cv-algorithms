import cv2 as cv
from run_images import run_images

def Sift(input):
  sift = cv.SIFT_create()
  key_points = sift.detect(input, None)

  return cv.drawKeypoints(input, key_points, None, color=(0, 255, 0))

run_images(Sift)
