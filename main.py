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

# Loads image as 80 * 80 pixels and saves it in a numpy array
img_raw = Image.open('mcdonalds.png')
img_raw = img_raw.resize((LOAD_IMG_WIDTH, LOAD_IMG_HEIGHT))
img = np.array(img_raw)
print(img)

# Removes alpha channel from an image if present
if img_raw.mode == 'RGBA':
    img = img[:,:,0:3]

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
    multiplied_output = input_data * filter
    output = np.sum(multiplied_output)

    min_filer_output = 150
    min_filer_string = ' '

    for filter_matrix, mapped_string in FILTER_PAIRS:
        multiplied_output = input_data * filter_matrix
        filter_output = np.sum(multiplied_output)

        if filter_output < min_filer_output:
            min_filer_output = filter_output
            min_filer_string = mapped_string


    print(min_filer_string, end='')

    # Checks that the output is within the range 0, 255 before returning
    if output > 255:
        return 255
    elif output < 0:
        return 0
    else:
        return output


def apply_filters(img_original, img_output, filter):
    for i in range(1, LOAD_IMG_HEIGHT - 1):
        for j in range(1, LOAD_IMG_WIDTH - 1):
            # Loads the pixel at location i, j and the along with the 8
            # surrounding it
            input_data = img_original[i - 1: i + 2, j - 1: j + 2]

            # Load the pixels as a 3 * 3 array (one int representing each pixel)
            input_data = input_data[:,:,0:1]
            input_data = input_data.reshape((3,3))

            # intput_data = input_data.astype('int32')

            # calculate the filter output
            filter_output = print_filter_output(input_data, filter)
            img_output[i - 1][j - 1] = filter_output


np.apply_along_axis(change_to_gray_scale, axis=2, arr=img)

img_output = np.zeros((48, 80, 3), dtype='uint8')

print('*' * 80)
# apply_filters(img, img_output, UNDERSCORE_FILTER)
apply_filters(img, img_output, FORWARDSLASH_FILTER)
# apply_filters(img, img_output, BACKSLASH_FILTER)


# print(img_output)
# print(img_output.shape)
print('*' * 80)

# image = Image.fromarray(np.uint8(img_output))
image = Image.fromarray(np.uint8(img))

# Save the image
image.save('output_image.png')

