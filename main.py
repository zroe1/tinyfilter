from PIL import Image # type: ignore
import numpy as np
from numpy.typing import NDArray
import shutil

LOAD_IMG_WIDTH = shutil.get_terminal_size().columns + 2
LOAD_IMG_HEIGHT  = int(LOAD_IMG_WIDTH * (5/8))

# Filters applied to the image to detect features
BACKSLASH_FILTER = np.array([[3, -1, -1], [-1, 3, -1], [-1, -1, 3]], dtype='int32')
FORWARDSLASH_FILTER = np.array([[-1, -1, 3], [-1, 3, -1], [3, -1, -1]], dtype='int32')
VERTICAL_BAR_FILTER = np.array([[-1, 3, -1], [-1, 3, -1], [-1, 3, -1]], dtype='int32')
HYPEN_FILTER = np.array([[-1, -1, -1],  [3, 4, 3], [-1, -1, -1]], dtype='int32')
UNDERSCORE_FILTER = np.array([[-1, -1, -1], [-1, -1, -1], [3, 4, 3]], dtype='int32')

# Filters applied to image and their corresponding ASCII feature
FILTER_PAIRS = [
    (BACKSLASH_FILTER, '\\'),
    (FORWARDSLASH_FILTER, '/'),
    (VERTICAL_BAR_FILTER, '|'),
    (HYPEN_FILTER, '-'),
    (UNDERSCORE_FILTER, '_')
]

def change_pixel_to_gray_scale(pixel: NDArray[np.uint8]):
    red: int = pixel[0]
    green: int = pixel[1]
    blue: int = pixel[2]

    # Apply the following formula to find the greyscale value for the pixel
    gray_scale_value = 0.2989 * red + 0.5870 * green + 0.1140 * blue

    # Change each color value in the pixel to the calculated greyscale value
    pixel[:] = int(gray_scale_value)

def print_filter_output(img_region: NDArray[np.uint8]):
    min_filer_output: int = 150
    min_filer_string: str = ' '

    # Finds the filter that maps the best and saves it's conesponding character
    # note: filter_matrix is a numpy array of type int32
    for filter_matrix, mapped_string in FILTER_PAIRS:
        multiplied_output = img_region * filter_matrix
        filter_output: int = np.sum(multiplied_output)

        if filter_output < min_filer_output:
            min_filer_output = filter_output
            min_filer_string = mapped_string
    
    print(min_filer_string, end='')

def print_img(img: NDArray[np.uint8]):
    for i in range(1, LOAD_IMG_HEIGHT - 1):
        for j in range(1, LOAD_IMG_WIDTH - 1):
            # Loads the pixel at location i, j and the along with the 8
            # surrounding it
            img_region = img[i - 1: i + 2, j - 1: j + 2]

            # Load the pixels as a 3 * 3 array (one int representing each pixel)
            img_region = img_region[:,:,0:1]
            img_region = img_region.reshape((3,3))

            print_filter_output(img_region)


def main() -> None:
    # Loads image as 80 * 80 pixels and saves it in a numpy array
    img_raw = Image.open('github.png')
    img_raw = img_raw.resize((LOAD_IMG_WIDTH, LOAD_IMG_HEIGHT))
    img: NDArray[np.uint8] = np.array(img_raw)

    # Removes alpha channel from an image if present
    if img_raw.mode == 'RGBA':
        img = img[:,:,0:3]
    
    # Changes image to grayscale
    np.apply_along_axis(change_pixel_to_gray_scale, axis=2, arr=img)

    print('*' * shutil.get_terminal_size().columns)
    print_img(img)
    print('*' * shutil.get_terminal_size().columns)
    

if __name__ == '__main__':
    main()