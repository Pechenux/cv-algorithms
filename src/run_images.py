import cv2 as cv
import os

# test = cv.imread()

input_folder = os.path.abspath('images')
output_folder = os.path.abspath('output')
images = os.listdir(input_folder)

def run_images(fun, flags = cv.IMREAD_COLOR):
    for image in images:
        image_path = os.path.join(input_folder, image)
        output_path = os.path.join(output_folder, image)
        print("Processing", image_path)
        cv.imwrite(output_path, fun(cv.imread(image_path, flags)))
