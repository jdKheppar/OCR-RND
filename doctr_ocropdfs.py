# -*- coding: utf-8 -*-
"""doctr_ocrOpdfs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wyy1tq4aTLqLFREKn4QGuQZlBMtBAOjQ
"""

#docTR
! pip install python-doctr
# for TensorFlow
! pip install "python-doctr[tf]"
# for PyTorch
! pip install "python-doctr[torch]"

!apt-get install -y poppler-utils
!pip install pdf2image

from pdf2image import convert_from_path
import os
import pandas as pd

from doctr.io import DocumentFile
from doctr.models import ocr_predictor
model = ocr_predictor(det_arch = 'db_resnet50',
                      reco_arch = 'crnn_vgg16_bn',
                      pretrained = True
                     )

# Function to convert PDFs to images
def convert_pdfs_to_images(input_folder, output_folder):

    # Get all PDF files in the input folder
    pdf_files = [file for file in os.listdir(input_folder) if file.endswith(".pdf")]

    # Initialize keras-ocr pipeline


    # Process each PDF
    for pdf_file in pdf_files:
        pdf_base_name = os.path.splitext(pdf_file)[0]
        pdf_file_path = os.path.join(input_folder, pdf_file)

        # Convert PDF to an image
        images = convert_from_path(pdf_file_path, fmt="jpeg")

        # Save the image to the output folder
        image_path = f"{output_folder}/{pdf_base_name}.jpeg"
        images[0].save(image_path)
        # read file
        img_DOCTR = DocumentFile.from_images(image_path)

        # use pre-trained model
        result = model(img_DOCTR)

        # export the result as a nested dict
        extract_info_DOCTR = result.export()
        output_txt_path = os.path.join(output_folder, f"{pdf_base_name}_output.txt")
        result_DOCTR=extract_info_DOCTR['pages']
        with open(output_txt_path, "w") as text_file:
          for i in result_DOCTR:

            for j in i['blocks']:
              for k in j['lines']:
                for l in k['words']:
                  print(l['value'])
                  text_file.write(f"{l['value']} ")
                text_file.write("\n")

# Example usage:
input_folder_path = "/content"  # Change this to the path of your input folder
output_folder_path = "/content/output_images"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Convert PDFs to images and extract text
convert_pdfs_to_images(input_folder_path, output_folder_path)

# read file
img_DOCTR = DocumentFile.from_images("crop.jpeg")

# use pre-trained model
result = model(img_DOCTR)

# export the result as a nested dict
extract_info_DOCTR = result.export()

result_DOCTR=extract_info_DOCTR['pages']
for i in result_DOCTR:

  for j in i['blocks']:
    for k in j['lines']:
      for l in k['words']:
        print(l['value'])

img_DOCTR1 = DocumentFile.from_images("2.jpeg")

# use pre-trained model
result1 = model(img_DOCTR1)

# export the result as a nested dict
extract_info_DOCTR1 = result1.export()
result_DOCTR1=extract_info_DOCTR1['pages']
for i in result_DOCTR1:

  for j in i['blocks']:
    for k in j['lines']:
      for l in k['words']:
        print(l['value'])
