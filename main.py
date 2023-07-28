from PIL import Image # type: ignore
import numpy as np

LOAD_IMG_WIDTH = 80
LOAD_IMG_HEIGHT  = 80

img_raw = Image.open('example_image.png')
img_raw = img_raw.resize((LOAD_IMG_WIDTH, LOAD_IMG_HEIGHT))
img = np.array(img_raw)

if img_raw.mode == 'RGBA':
    print(img_raw.mode)
    img = img[:,:,0:3]

image = Image.fromarray(np.uint8(img))

# Save the image
image.save('output_image.png')

