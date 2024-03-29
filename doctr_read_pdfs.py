# -*- coding: utf-8 -*-
"""doctr_read_pdfs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y83EztTTu92FhcC2vcZGB0WlbJwdFjRw
"""

!pip install pdf2image pillow "python-doctr[tf]" "python-doctr[torch]" python-doctr
!apt-get install -y poppler-utils
import os
from pdf2image import convert_from_path
from PIL import Image
from doctr.io import DocumentFile
from doctr.models import ocr_predictor

Image.MAX_IMAGE_PIXELS = None

# Example usage:
input_folder = "/content"  # Change this to the path of your input folder
output_folder = "/content/output_texts"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Convert PDFs to images and extract text using python-doctr
# Get all PDF files in the input folder
pdf_files = [file for file in os.listdir(input_folder) if file.endswith(".pdf")]

# Initialize python-doctr OCR model
model = ocr_predictor(det_arch='db_resnet50', reco_arch='crnn_vgg16_bn', pretrained=True)

# Process each PDF
for pdf_file in pdf_files:
    pdf_base_name = os.path.splitext(pdf_file)[0]
    pdf_file_path = os.path.join(input_folder, str(pdf_file))
    print(pdf_file_path)
    # Convert PDF to an image using python-doctr
    #img_doctr = DocumentFile.from_images(pdf_file_path)
    images = convert_from_path(str(pdf_file_path))
    # Use pre-trained model
    result = model(images[0])

    # Export the result as a nested dict
    extract_info_doctr = result.export()
    result_doctr = extract_info_doctr['pages']

    # Save extracted text to a text file
    output_txt_path = os.path.join(output_folder, f"{pdf_base_name}_output.txt")
    with open(output_txt_path, "w") as text_file:
        text_file.write(f"Extracted text from {pdf_file}:\n")
        for i in result_doctr:
            for j in i['blocks']:
                for k in j['lines']:
                    for l in k['words']:
                        text_file.write(f"{l['value']} ")
                    text_file.write("\n")

    print(f"Extracted text from {pdf_file} and saved to {output_txt_path}")