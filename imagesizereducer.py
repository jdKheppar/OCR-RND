# -*- coding: utf-8 -*-
"""ImageSizeReducer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x5XN70XP6dDAnGCNB26MtgiDS7bCgeC9
"""

!pip install pillow
Image.MAX_IMAGE_PIXELS = None

from PIL import Image
filename = '4L.jpg'
img = Image.open(filename)
img.save(filename, "jpeg")#, quality=10

import os
from PIL import Image
filename = '4L.jpg'
img = Image.open(filename)
new_filename = os.path.splitext(filename)[0] + '.jpeg'
img.save(new_filename, "jpeg")#, quality=10