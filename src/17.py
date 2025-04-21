import cv2 as cv
from run_images import run_images

def ShiftColorPalette(input):
    hsv = cv.cvtColor(input, cv.COLOR_BGR2HSV)
    h, s, v = cv.split(hsv)
    
    hue_shift = 70
    shift_h = (h + hue_shift) % 180
    shift_hsv = cv.merge([shift_h, s, v])

    return cv.cvtColor(shift_hsv, cv.COLOR_HSV2BGR)

run_images(ShiftColorPalette)
