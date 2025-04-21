import cv2 as cv
import os

# test = cv.imread()

input_folder = os.path.abspath('images')
output_folder = os.path.abspath('output')
images = os.listdir(input_folder)

def run_images(fun, flags = cv.IMREAD_COLOR):
    for image in images:
        image_path = os.path.join(input_folder, image)
        print("Processing", image_path)
        output = fun(cv.imread(image_path, flags))
        if isinstance(output, list):
            for i in range(len(output)):
                output_path = os.path.join(output_folder, str(i) + image)
                cv.imwrite(output_path, output[i])
        else:
            output_path = os.path.join(output_folder, image)
            cv.imwrite(output_path, output)
