# -*- coding: utf-8 -*-
"""easy_ocr_Images.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dcsO3AvskoSAFta6X4fgm624BnJf3luo
"""

# installation
!pip install easyocr
#EasyOCR
import easyocr
import os
!pip install pillow
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
reader = easyocr.Reader(['en'])

uploaded_files = ['crop.jpeg']

# Create a folder to store text files

output_directory = '/OCR Processed'
os.makedirs(output_directory, exist_ok=True)

# Process each uploaded .jpeg file
for jpeg_file in uploaded_files:

    img = Image.open(jpeg_file)

    # Perform OCR on the current .jpeg file
    extract_info = reader.readtext(img)

    # Write results to a text file
    txt_file = os.path.join(output_directory, os.path.splitext(jpeg_file)[0] + '.txt')
    with open(txt_file, 'w') as txt_file:
        for result in extract_info:
            txt_file.write(result[1] + '\n')

    print(f"Processed {jpeg_file}. Results stored in {txt_file}")

# Create a zip file with all text files
import shutil
shutil.make_archive('/content/output_text_files', 'zip', output_directory)

!pip install keras-ocr -q
#Keras OCR
import keras_ocr

pipeline = keras_ocr.pipeline.Pipeline()
keras_extract_info = pipeline.recognize(["1.jpeg"])
for result in keras_extract_info:
    for text_info in result:
        text = text_info[0]
        print(text)

keras_extract_info = pipeline.recognize(["2.jpeg"])
for result in keras_extract_info:
    for text_info in result:
        text = text_info[0]
        print(text)

keras_extract_info = pipeline.recognize(["3.jpeg"])
for result in keras_extract_info:
    for text_info in result:
        text = text_info[0]
        print(text)



#keras ocr continue
import pandas as pd
diz_cols = {'word':[],'box':[]}
for el in extract_info[0]:
    diz_cols['word'].append(el[0])
    diz_cols['box'].append(el[1])
kerasocr_res = pd.DataFrame.from_dict(diz_cols)
# Set the option to display all rows


# Print the DataFrame
print(kerasocr_res)



extract_info_S = reader.readtext("4L.jpg")
for result in extract_info_S:
    print(result[1])

extract_info_S1 = reader.readtext("54.jpeg")
for result in extract_info_S1:
    print(result[1])