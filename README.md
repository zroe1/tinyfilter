# tinyfilter
<img width="1423" alt="Screenshot 2023-08-05 at 4 52 21 PM" src="https://github.com/zroe1/tinyfilter/assets/114773939/488e61be-3431-444c-9fcc-8ae8944c8b59">
</br></br>  

tinyfilter [^1] is the computer vision equivalent to micrograd. It convert images into ASCII art using the principles of CNNs (convolutional neural networks).  
</br>
Unlike other tools of its type, which map pixel darkness to an ASCII character, tinyfilter uses filters and convolution to detect features in an image and prints ASCII characters that correspond to them. This leads to much better results compared to other libraries for smaller images.

[^1]: For consistency, the first letter in "tinyfilter" is always lowercase, even when it begins a sentence.

## Installation
To install tinyfilter locally run the command below. When installing python packages such as tinyfilter, I recommend using a virtual environment.

    pip install tinyfilter

## Usage
To print an image as ASCII characters using tinyfilter run the following command in your terminal. (Replace "image.png" with the name of your image.)

     tinyfilter image.png

You can also import tinyfilter inside a python file or interpreter to do the same thing:

```
from tinyfilter import tiny_print
tiny_print('image.png')
```

## Why tinyfilter wins

<img width="829" alt="Screenshot 2023-08-05 at 7 53 28 PM" src="https://github.com/zroe1/tinyfilter/assets/114773939/75eb9d2b-c0e9-4c33-80c5-227fd9cc3a5e">

While other python packages have features that tinyfilter doesn't yet support, tinyfilter clearly does win at one thing: recognizing the important features in an image and focusing on those. <b>In the example above tinyfilter and Ascii-magic bother print images that are 80 columns wide.</b> The difference is that tinyfilter's output is based on where there are edges in the image while Ascii-magic only focuses on where the image is dark and where is it bright.

## Resources and sources
<ul>
  <li><b><a href="https://pillow.readthedocs.io/en/stable/about.html">Pillow</a></b> is a dependency for tinyfilter</li>
  <li><b><a href="https://numpy.org/">numpy</a></b> is a dependency for tinyfilter</li>
  <li><b><a href="https://github.com/python/mypy">mypy</a></b> was used for type checking</li>
  <li><b><a href="https://github.com/psf/black">Black</a></b> was used for python code formatting</li>
</ul>


