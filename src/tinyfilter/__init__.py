"""Loads an image and prints it to the console as ASCII characters.

This file applies convolution to an image to detect small features in an image
that translate directly to ASCII characters. The result of the operation is
printed to the console as it occurs.
"""
from PIL import Image  # type: ignore
import numpy as np
from numpy.typing import NDArray
import shutil
import argparse

LOAD_IMG_WIDTH = shutil.get_terminal_size().columns + 2
LOAD_IMG_HEIGHT = int(LOAD_IMG_WIDTH * (5 / 8))

# Filters applied to the image to detect features
BACKSLASH_FILTER = np.array([[3, -1, -1], [-1, 3, -1], [-1, -1, 3]], dtype="int32")
FORWARDSLASH_FILTER = np.array([[-1, -1, 3], [-1, 3, -1], [3, -1, -1]], dtype="int32")
VERTICAL_BAR_FILTER = np.array([[-1, 3, -1], [-1, 3, -1], [-1, 3, -1]], dtype="int32")
HYPEN_FILTER = np.array([[-1, -1, -1], [3, 4, 3], [-1, -1, -1]], dtype="int32")
UNDERSCORE_FILTER = np.array([[-1, -1, -1], [-1, -1, -1], [3, 4, 3]], dtype="int32")


# Filters applied to image and their corresponding ASCII feature
FILTER_PAIRS = [
    (BACKSLASH_FILTER, "\\"),
    (FORWARDSLASH_FILTER, "/"),
    (VERTICAL_BAR_FILTER, "|"),
    (HYPEN_FILTER, "-"),
    (UNDERSCORE_FILTER, "_"),
]


def change_pixel_to_gray_scale(pixel: NDArray[np.uint8]) -> None:
    """Modifies a pixel in place to it's grayscale equivalent.

    Args:
        pixel: A 1D numpy array of length 3 representing an RGB pixel
    """
    red: int = pixel[0]
    green: int = pixel[1]
    blue: int = pixel[2]

    gray_scale_value = 0.2989 * red + 0.5870 * green + 0.1140 * blue

    pixel[:] = int(gray_scale_value)


def print_filter_output(img_region: NDArray[np.uint8]) -> None:
    """Prints the character with the most present filter in img_region.

    Args:
        img_region: a 3 * 3 numpy array. Each number corresponds to a greyscale
          pixel in the original image.
    """
    min_filer_output: int = 150
    min_filer_string: str = " "

    for filter_matrix, mapped_string in FILTER_PAIRS:
        # note: filter_matrix is a numpy array of type int32 so
        # multiplied_output inherits the type int32 (not uint8)
        multiplied_output = img_region * filter_matrix
        filter_output: int = np.sum(multiplied_output)

        if filter_output < min_filer_output:
            min_filer_output = filter_output
            min_filer_string = mapped_string

    print(min_filer_string, end="")


def print_grayscale_img(img: NDArray[np.uint8]) -> None:
    """Prints a grayscale image as ASCII characters to console.

    Args:
        img: a numpy array of grayscale pixels (shape = (x, x, 3))
    """
    for i in range(1, LOAD_IMG_HEIGHT - 1):
        for j in range(1, LOAD_IMG_WIDTH - 1):
            # Loads a 9 pixel region of the image
            img_region = img[i - 1 : i + 2, j - 1 : j + 2]

            # Load the pixels as a 3 * 3 array (one int representing the
            # grayscale value of each pixel in the region)
            img_region = img_region[:, :, 0:1]
            img_region = img_region.reshape((3, 3))

            print_filter_output(img_region)


def tiny_print(img_filename=None) -> None:
    """Loads an image and prints it as ASCII characters to the console"""
    if img_filename == None:
        parser = argparse.ArgumentParser(
            prog="tinyfilter",
            description="What the program does",
            epilog="Text at the bottom of help",
        )
        parser.add_argument("filename")

        args = parser.parse_args()
        img_raw = Image.open(args.filename)
    else:
        img_raw = Image.open(img_filename)

    # checks if the image type is supported by tinyfilter
    if img_raw.mode != "RGB" and img_raw.mode != "RGBA":
        parser.error('''
    
    Image mode was {}. Currently tinyfilter only supports modes of "RGB" and 
    "RGBA." To learn more about image modes visit the Pillow (a dependency 
    of tinyfilter) documentation:

    https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes
        '''.format(img_raw.mode))

    img_raw = img_raw.resize((LOAD_IMG_WIDTH, LOAD_IMG_HEIGHT))
    img: NDArray[np.uint8] = np.array(img_raw)

    # Removes alpha channel from an image if present
    if img_raw.mode == "RGBA":
        img = img[:, :, 0:3]

    np.apply_along_axis(change_pixel_to_gray_scale, axis=2, arr=img)

    print("*" * shutil.get_terminal_size().columns)
    print_grayscale_img(img)
    print("*" * shutil.get_terminal_size().columns)


if __name__ == "__main__":
    tiny_print()
