# tinyfilter
<img width="1423" alt="Screenshot 2023-08-05 at 4 52 21 PM" src="https://github.com/zroe1/tinyfilter/assets/114773939/488e61be-3431-444c-9fcc-8ae8944c8b59">
</br></br>  

tinyfilter [^1] is the computer vision equivalent to micrograd. It convert images into ASCII art using the principles of CNNs (convolutional neural networks).  
</br>
Unlike other tools of its type, which map pixel darkness to an ASCII character, tinyfilter uses filters and convolution to detect features in an image and prints ASCII characters that correspond to them. This leads to much better results for smaller images.

[^1]: For consistency, the first letter in "tinyfilter" is always lowercase, even when it begins a sentence.

## Using tinyfilter
First you will have to install tinyfilter locally. I recommend using a virtual environment before installing python packages like tinyfilter.  

    pip install tinyfilter

Then run

     tinyfilter image.png

## Resources and sources
<ul>
  <li><b><a href="https://pillow.readthedocs.io/en/stable/about.html">Pillow</a></b> is a dependency for tinyfilter</li>
  <li><b><a href="https://numpy.org/">numpy</a></b> is a dependency for tinyfilter</li>
  <li><b><a href="https://github.com/python/mypy">mypy</a></b> was used for type checking</li>
  <li><b><a href="https://github.com/psf/black">Black</a></b> was used for python code formatting</li>
</ul>


