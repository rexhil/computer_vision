import cv2
import numpy as np
import sys


def main(file_name, image_format):
    orig_image = cv2.imread(file_name)  # Read image file
    converted_image = convert_image(orig_image, image_format)
    a, b, c = cv2.split(converted_image)
    na, nb, nc = image_dimension_fix([a, b, c])
    top = np.hstack((converted_image, na))
    bottom = np.hstack((nb, nc))
    final_image = np.vstack((top, bottom))
    cv2.namedWindow('image', cv2.WINDOW_FREERATIO)
    cv2.imshow('image', final_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def convert_image(orig_image, image_format):
    """
    Converts given image to image format passed in second argument
    :param orig_image: original image MAT
    :param image_format: image for to convert to
    :return: converted image MAT
    """
    image_format_dict = {
        'LAB': cv2.COLOR_BGR2Lab,
        'XYZ': cv2.COLOR_BGR2XYZ,
        'YCrCb': cv2.COLOR_BGR2YCrCb,
        'HSB': cv2.COLOR_BGR2HSV,
        'RGB': None
    }
    if image_format not in image_format_dict.keys():
        print("Incorrect image format, options are: LAB, XYZ, YCrCb, HSB)")
    elif img_format == "RGB":
        return orig_image
    return cv2.cvtColor(orig_image, image_format_dict[image_format]) # change image to image format specified


def image_dimension_fix(images: list):
    """
    Original image have 3 dimension and components have 2 dimensions.
    :param images: 3 images (all 3 Component of image)
    :return: all component image converted to RGB for adding dimension
    """
    _list = []
    for image in images:
        _list.append(cv2.cvtColor(image, cv2.COLOR_GRAY2RGB))
    return _list


if __name__ == '__main__':
    img_format = sys.argv[2]
    file_name = sys.argv[1]
    main(file_name, img_format)
