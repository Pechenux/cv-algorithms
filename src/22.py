import cv2 as cv
import numpy as np
from run_images import run_images

r = 20

def FourierFast(input):
    gray = cv.cvtColor(input, cv.COLOR_BGR2GRAY)

    f_transform = np.fft.fft2(gray)
    f_transform_shifted = np.fft.fftshift(f_transform)

    rows, cols = gray.shape
    mask = np.ones((rows, cols), np.uint8)

    center = [rows // 2, cols // 2]
    x, y = np.ogrid[:rows, :cols]
    mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r * r
    mask[mask_area] = 0

    f_transform_filtered = f_transform_shifted * mask

    return np.fft.ifft2(np.fft.ifftshift(f_transform_filtered)).real

run_images(FourierFast)
