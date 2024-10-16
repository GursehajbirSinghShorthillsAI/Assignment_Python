import os
import fitz  # PyMuPDF for PDFs
import csv
from PIL import Image
from docx import Document  # For DOCX files
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import pptx
from abc import ABC, abstractmethod
import csv
from PyPDF2 import PdfReader
import json
from pdf_loader import PDFLoader
from docx_loader import DOCXLoader

output_base_dir = os.getcwd()  # Base directory for output

#Path to the sample file
file_path = 'Sample_file/sample.pdf'  # Update this for docx or pdf
# Function to create segregated output directories
def create_output_dirs(output_base_dir, file_type):
    output_dir = os.path.join(output_base_dir, f"Output_{file_type}")
    subfolders = ['text', 'images', 'tables', 'links', 'metadata']
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create subdirectories for text, images, tables, and links
    for folder in subfolders:
        os.makedirs(os.path.join(output_dir, folder), exist_ok=True)
    
    return output_dir





def save_text_to_file(text, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

def save_links_to_file(links, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["URL"])
        for link in links:
            writer.writerow([link])

def save_tables_to_csv(tables):
    for index, table in enumerate(tables):
        csv_path = os.path.join(output_dir, f"table_{index + 1}.csv")
        with open(csv_path, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(table)

def save_metadata_to_json(metadata, file_name):
    json_path = os.path.join(output_dir, file_name)
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(metadata, json_file, indent=4)

#Determine if file is PDF or DOCX and process accordingly
if file_path.endswith('.pdf'):
    # Processing the PDF
    output_dir = create_output_dirs(output_base_dir, 'pdf')
    pdf_loader = PDFLoader(file_path)
    pdf_loader.load_file()

    # Extract text and save to a text file
    text = pdf_loader.extract_text()
    save_text_to_file(text, os.path.join(output_dir, "extracted_text.txt"))

    # Extract links and save to a CSV file
    links = pdf_loader.extract_links()
    save_links_to_file(links, os.path.join(output_dir, "extracted_links.csv"))

    # Extract images and save to the output directory
    images = pdf_loader.extract_images()
    print(f"Images extracted and saved at: {images}")

    # Extract tables and save to CSV files
    tables = pdf_loader.extract_tables()
    save_tables_to_csv(tables)

    detailed_metadata = pdf_loader.extract_detailed_metadata()
    save_metadata_to_json(detailed_metadata, "pdf_detailed_metadata.json")
    print(f"Detailed PDF metadata saved to pdf_detailed_metadata.json")

elif file_path.endswith('.docx'):
    # Processing the DOCX
    output_dir = create_output_dirs(output_base_dir, 'docx')
    docx_loader = DOCXLoader(file_path)

    # Extract text and save to a text file
    text = docx_loader.extract_text()
    save_text_to_file(text, os.path.join(output_dir, "extracted_text.txt"))

    # Extract links and save to a CSV file
    links = docx_loader.extract_links()
    save_links_to_file(links, os.path.join(output_dir, "extracted_links.csv"))

    # Extract images and save to the output directory
    images = docx_loader.extract_images()
    print(f"Images extracted and saved at: {images}")

    # Extract tables and save to CSV files
    tables = docx_loader.extract_tables()
    save_tables_to_csv(tables)

    detailed_metadata = docx_loader.extract_detailed_metadata()
    save_metadata_to_json(detailed_metadata, "docx_detailed_metadata.json")
    print(f"Detailed DOCX metadata saved to docx_detailed_metadata.json")

#Determine whether the file is PDF or DOCX and create output directories accordingly
# if file_path.endswith('.pdf'):
#     output_dir = create_output_dirs(output_base_dir, 'pdf')
#     pdf_loader = PDFLoader(file_path, output_dir)
#     pdf_loader.load_file()

#     # Perform extraction operations
#     pdf_loader.extract_text()
#     pdf_loader.extract_images()
#     pdf_loader.extract_links()
#     pdf_loader.extract_tables()

# elif file_path.endswith('.docx'):
#       output_dir = create_output_dirs(output_base_dir, 'docx')
#       docx_loader = DOCXLoader(file_path, output_dir)
    
#       #Perform extraction operations for DOCX...
#       docx_loader.extract_text()
#       docx_loader.extract_images()
#       docx_loader.extract_links()
#       docx_loader.extract_tables()

print("Processing complete! Check the 'output' folder for results.")

print("File processing complete!")







