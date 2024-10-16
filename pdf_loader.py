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


class PDFLoader:
    def __init__(self, file_path, output_dir):
        self.file_path = file_path
        self.output_dir = output_dir
        self.doc = None

    def load_file(self):
        # Open the PDF file using PyMuPDF
        self.doc = fitz.open(self.file_path)
        print(f"PDF {self.file_path} successfully loaded.")
        return self.doc

    def extract_text(self):
        # Extract text from each page
        text = ""
        for page_num in range(len(self.doc)):
            page = self.doc.load_page(page_num)
            text += page.get_text("text")
        
        # Save text in the "text" subfolder
        text_path = os.path.join(self.output_dir, 'text', 'extracted_text.txt')
        with open(text_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Text extracted and saved at: {text_path}")


    def extract_links(self):
        links = []
        link_folder = os.path.join(self.output_dir, 'links')
        link_csv_path = os.path.join(link_folder, "extracted_links.csv")
        for page_num in range(len(self.doc)):
            page = self.doc.load_page(page_num)
            links_on_page = page.get_links()
            for link in links_on_page:
                if link.get("uri"):
                    links.append({
                        "page": page_num + 1,
                        "uri": link.get("uri")
                    })

        # Save links in the "links" subfolder
        with open(link_csv_path, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Page", "URL"])
            for link in links:
                writer.writerow([link["page"], link["uri"]])
        print(f"Links extracted and saved at: {link_csv_path}")
        return links
    
    def extract_images(self):
        images = []
        image_folder = os.path.join(self.output_dir, 'images')
        for page_num in range(len(self.doc)):
            page = self.doc.load_page(page_num)
            image_list = page.get_images(full=True)
            for image_index, img in enumerate(image_list):
                xref = img[0]
                base_image = self.doc.extract_image(xref)
                img_bytes = base_image["image"]
                img_ext = base_image["ext"]
                img_path = os.path.join(image_folder, f"image_page_{page_num + 1}_{image_index}.{img_ext}")
                with open(img_path, "wb") as img_file:
                    img_file.write(img_bytes)
                images.append(img_path)
        print(f"Images extracted and saved at: {image_folder}")
        return images
    

    def extract_tables(self):
        # Extract tables (simplified, as PDFs aren't straightforward for table extraction)
        tables = []
        table_folder = os.path.join(self.output_dir, 'tables')
        for page_num in range(len(self.doc)):
            page = self.doc.load_page(page_num)
            text = page.get_text("text")
            if "table" in text.lower():
                table_data = {
                    "page": page_num + 1,
                    "content": text
                }
                tables.append(table_data)
                # Save each table in a CSV file
                table_csv_path = os.path.join(table_folder, f"table_page_{page_num + 1}.csv")
                with open(table_csv_path, "w", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow([text])
                print(f"Table from page {page_num + 1} saved at: {table_csv_path}")
        return tables

    
    def extract_detailed_metadata(self):
        # Extract fonts, sizes, and other page-specific information
        metadata = []
        for page_num in range(len(self.doc)):
            page = self.doc.load_page(page_num)
            text_instances = page.get_text("dict")["blocks"]  # Get text blocks
            page_metadata = []
            for block in text_instances:
                if block['type'] == 0:  # Type 0 means text block
                    for line in block['lines']:
                        for span in line['spans']:
                            page_metadata.append({
                                "font": span['font'],
                                "size": span['size'],
                                "color": span['color'],
                                "text": span['text']
                            })
            metadata.append({
                "page": page_num + 1,
                "fonts": page_metadata
            })
        return metadata
