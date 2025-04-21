import numpy as np
from run_images import run_images

def Warmer(input):
    return np.clip(input * [0.65, 1, 1.4], 0, 255)

run_images(Warmer)
