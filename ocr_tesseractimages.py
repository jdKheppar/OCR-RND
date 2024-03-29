# -*- coding: utf-8 -*-
"""ocr_tesseractImages.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12waBRHteU7HztoLjQQgWTUNQOJnDwwWq
"""

!pip install pdf2image pytesseract pillow
!apt-get install -y poppler-utils#for convertingt pdf to images
import os
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

Image.MAX_IMAGE_PIXELS = None#for ignoring the warning in image pixels

!sudo apt-get install tesseract-ocr
!pip install pytesseract

def extract_text_from_image(image_path):
    text = pytesseract.image_to_string(Image.open(image_path), lang='eng')
    return text

# Get the full path of the current directory
current_directory = os.getcwd()

# Get all PDF files in the current directory
pdf_files = [file for file in os.listdir() if file.endswith(".pdf")]

# Process each PDF
for pdf_file in pdf_files:
    pdf_file_base = os.path.splitext(os.path.basename(pdf_file))[0]
    pdf_file_path = os.path.join(current_directory, pdf_file)

    print(pdf_file)

    # Convert PDF to images
    images = convert_from_path(pdf_file_path)

    # Process each image
    for i, image in enumerate(images):
        # Extract text using Tesseract OCR
        image_path = f"{pdf_file_base}_page_{i + 1}.png"
        image.save(image_path)

        text_tesseract = extract_text_from_image(image_path)

        # Save text to a file with the same name as the PDF
        output_filename_tesseract = f"{pdf_file_base}_page_{i + 1}_tesseract.txt"
        with open(output_filename_tesseract, "w") as text_file_tesseract:
            text_file_tesseract.write(text_tesseract)

    print(f"Processed {len(images)} pages from {pdf_file}")