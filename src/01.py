import cv2 as cv
from run_images import run_images

def Orb(input):
  orb = cv.ORB_create()
  key_points, _ = orb.detectAndCompute(input, None)

  return cv.drawKeypoints(input, key_points, None, color=(0, 255, 0))

run_images(Orb, cv.IMREAD_GRAYSCALE)
