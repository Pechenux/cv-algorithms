import cv2 as cv
from run_images import run_images

def Colder(input):
    white_balancer = cv.xphoto.createSimpleWB()
    white_balancer.setP(5)
    return white_balancer.balanceWhite(input)

run_images(Colder)
