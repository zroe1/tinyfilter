# tinyfilter
<img width="1423" alt="Screenshot 2023-08-05 at 4 52 21 PM" src="https://github.com/zroe1/tinyfilter/assets/114773939/488e61be-3431-444c-9fcc-8ae8944c8b59">  
</br></br>  
<p align="center">
<a href="https://pypi.org/project/tinyfilter/0.1.7/"><img alt="link to PyPi" src="https://img.shields.io/badge/pypi-v0.1.7-brightgreen"></a>
<a href="https://github.com/zroe1/tinyfilter/blob/main/LICENSE"><img alt="link to license" src="https://img.shields.io/badge/License-MIT-purple"></a>
<a href="https://github.com/psf/black/tree/main"><img alt="link to license" src="https://img.shields.io/badge/code%20style-black-black"></a>
</p> 

tinyfilter [^1] is the computer vision equivalent to Andrej Karpathy's <a href="https://github.com/karpathy/micrograd">micrograd</a>. It convert images into ASCII art using the principles of CNNs (convolutional neural networks).  
</br>
Unlike other tools of its type, which map pixel darkness to an ASCII character, tinyfilter uses filters and convolution to detect features in an image and prints ASCII characters that correspond to them. This leads to much better results compared to other libraries, especially for smaller images.

[^1]: For consistency, the first letter in "tinyfilter" is always lowercase, even when it begins a sentence.

## Installation
To install tinyfilter locally run the command below. When installing python packages such as tinyfilter, I recommend using a virtual environment, but this is optional.

    pip install tinyfilter

## How to use tinyfilter
To print an image as ASCII characters using tinyfilter run the following command in your terminal. (Replace "image.png" with the name of your image.)

     tinyfilter image.png

You can also import tinyfilter inside a python file or interpreter to do the same thing:

```python
from tinyfilter import tiny_print
tiny_print('image.png')
```
<b>NOTE: You do not need to specify how many columns wide you want your image to be. tinyfilter automatically prints the image with the exact amount of columns wide your terminal window was at the time the function was called.</b>

## Why tinyfilter wins

<img width="829" alt="Screenshot 2023-08-05 at 7 53 28 PM" src="https://github.com/zroe1/tinyfilter/assets/114773939/75eb9d2b-c0e9-4c33-80c5-227fd9cc3a5e">

While other python packages have features that tinyfilter doesn't yet support, tinyfilter clearly does win at one thing: recognizing the important features in an image and focusing on those. <b>In the example above tinyfilter and Ascii-magic bother print images that are 80 columns wide.</b> The difference is that tinyfilter's output is based on where there are edges in the image while Ascii-magic only focuses on where the image is dark and where is it bright.

## Examples of tinyfilter
### Github logo:
<img width="833" alt="Screenshot 2023-08-05 at 9 53 08 PM" src="https://github.com/zroe1/tinyfilter/assets/114773939/ae411367-1bd7-442e-a27e-6c2c31e69d5b">  

The numbers at the top of the images show how many columns the output is in ASCII characters. The example shows how depite losing large amounts of detail as the image gets smaller, tinyfilter is able to retain important elements of the orginal.

### Balloon dog (110 columns):
<img width="729" alt="Screenshot 2023-08-05 at 10 02 38 PM" src="https://github.com/zroe1/tinyfilter/assets/114773939/3b3b4d4b-6d69-4bc5-af65-eddeaf900cc9">

The balloon dog is a good example of edge detection (notice tinyfilter doesn't print anything when the balloon is solid purple but prints a line when the image transfers to white).

### Einstein (271 columns):
<img width="740" alt="Screenshot 2023-08-05 at 10 14 57 PM" src="https://github.com/zroe1/tinyfilter/assets/114773939/fa33be16-8c10-43bc-b8cb-3e38bcf5e7ac">

The Einstein image is a good example of how tinyfilter can scale to large images.

## How tinyfilter works (it's simpler than you think)

To make sense of the terms in this section you will need a little background on CNNs (convolutional neural networks). The design of tinyfilter is based on the technique these networks use called convolution. Reading the first half of <a href="https://www.ibm.com/topics/convolutional-neural-networks">this source</a> from IBM should get you up to speed. 

The most important part of an image is the lines. Thats what tinyfilter detects using only 5 filters which I hardcoded as numpy arrays (shown below).  When the filters are applied to an image, tinyfiler calculates if the feature the filter is detecting for is present. If it is, tinyfilter prints the ASCII character that corresponds to the feature.

```python
BACKSLASH_FILTER = np.array([[3, -1, -1], [-1, 3, -1], [-1, -1, 3]], dtype="int32")
FORWARDSLASH_FILTER = np.array([[-1, -1, 3], [-1, 3, -1], [3, -1, -1]], dtype="int32")
VERTICAL_BAR_FILTER = np.array([[-1, 3, -1], [-1, 3, -1], [-1, 3, -1]], dtype="int32")
HYPEN_FILTER = np.array([[-1, -1, -1], [3, 4, 3], [-1, -1, -1]], dtype="int32")
UNDERSCORE_FILTER = np.array([[-1, -1, -1], [-1, -1, -1], [3, 4, 3]], dtype="int32")
```

## Resources and sources
For more information about resources and their licenses, visit THANKS.txt under this repository.

<ul>
  <li><b><a href="https://pillow.readthedocs.io/en/stable/about.html">Pillow</a></b> is a dependency for tinyfilter</li>
  <li><b><a href="https://numpy.org/">numpy</a></b> is a dependency for tinyfilter</li>
  <li><b><a href="https://github.com/python/mypy">mypy</a></b> was used for type checking</li>
  <li><b><a href="https://github.com/psf/black">Black</a></b> was used for python code formatting</li>
  <li><b><a href="https://www.youtube.com/watch?v=NmLK_WQBxB4">This MIT lecutre</a></b> is a great resource for learning about CNNs and filters. I learned a lot from it and this project would not have been possible without it.</li>
</ul>


