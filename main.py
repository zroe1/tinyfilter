from PIL import Image # type: ignore
import numpy as np

LOAD_IMG_WIDTH = 82
LOAD_IMG_HEIGHT  = 50


BACKSLASH_FILTER = np.array([[3, -1, -1], [-1, 3, -1], [-1, -1, 3]], dtype='int32')
FORWARDSLASH_FILTER = np.array([[-1, -1, 3], [-1, 3, -1], [3, -1, -1]], dtype='int32')
VERTICAL_BAR_FILTER = np.array([[-1, 3, -1], [-1, 3, -1], [-1, 3, -1]], dtype='int32')
HYPEN_FILTER = np.array([[-1, -1, -1],  [3, 4, 3], [-1, -1, -1]], dtype='int32')
UNDERSCORE_FILTER = np.array([[-1, -1, -1], [-1, -1, -1], [3, 4, 3]], dtype='int32')


FILTER_PAIRS = [
    (BACKSLASH_FILTER, '\\'),
    (FORWARDSLASH_FILTER, '/'),
    (VERTICAL_BAR_FILTER, '|'),
    (HYPEN_FILTER, '-'),
    (UNDERSCORE_FILTER, '_')
]

def change_to_gray_scale(pixel):
    # Gets each color value for the pixel passed in
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    # Apply the following formula to find the greyscale value for the pixel
    gray_scale_value = 0.2989 * red + 0.5870 * green + 0.1140 * blue

    # Change each color value in the pixel to the calculated greyscale value
    pixel[:] = int(gray_scale_value)

def print_filter_output(input_data, filter):
    min_filer_output = 150
    min_filer_string = ' '

    for filter_matrix, mapped_string in FILTER_PAIRS:
        multiplied_output = input_data * filter_matrix
        filter_output = np.sum(multiplied_output)

        if filter_output < min_filer_output:
            min_filer_output = filter_output
            min_filer_string = mapped_string


    print(min_filer_string, end='')

def print_img(img_original):
    for i in range(1, LOAD_IMG_HEIGHT - 1):
        for j in range(1, LOAD_IMG_WIDTH - 1):
            # Loads the pixel at location i, j and the along with the 8
            # surrounding it
            input_data = img_original[i - 1: i + 2, j - 1: j + 2]

            # Load the pixels as a 3 * 3 array (one int representing each pixel)
            input_data = input_data[:,:,0:1]
            input_data = input_data.reshape((3,3))

            # print filter output
            print_filter_output(input_data, filter)


def main():
    # Loads image as 80 * 80 pixels and saves it in a numpy array
    img_raw = Image.open('nike2.png')
    img_raw = img_raw.resize((LOAD_IMG_WIDTH, LOAD_IMG_HEIGHT))
    img = np.array(img_raw)

    # Removes alpha channel from an image if present
    if img_raw.mode == 'RGBA':
        img = img[:,:,0:3]
    
    np.apply_along_axis(change_to_gray_scale, axis=2, arr=img)

    print('*' * 80)
    print_img(img)
    print('*' * 80)
    

if __name__ == '__main__':
    main()