# Text, Images, Tables and Links Extractor from PDF, DOCX, and PPT
This project extracts text, images, links, tables, and detailed metadata (fonts, sizes, and styles) from PDF and DOCX files. The metadata is saved in a JSON file for easier access. The project is designed to work with both PDF and DOCX files using Python libraries such as PyMuPDF, python-docx, and Pillow.
## Features
- Text Extraction: Extracts all the text content from PDF and DOCX files.
- Image Extraction: Extracts images from PDF and DOCX files and saves them in a specified output directory.
- Link Extraction: Extracts all hyperlinks from PDF and DOCX files and saves them in a CSV file.
- Table Extraction: Extracts tables from PDF and DOCX files and saves them in CSV format.
- Metadata Extraction: Extracts detailed metadata (fonts, sizes, text styling) from both PDF and DOCX files and saves it in a JSON file.

## Directory Structure
``` sql
.
├── Output/               # All output files (text, images, links, tables, metadata) are saved here
├── sample.pdf            # Sample PDF file (replace with your file)
├── sample.docx           # Sample DOCX file (replace with your file)
├── script.py             # Main script to run the document extraction
├── README.md             # This README file
└── requirements.txt      # List of required Python libraries
```
## Requirements
Before running the project, ensure you have the following Python libraries installed:

- PyMuPDF (fitz) - For processing PDF files.
- python-docx - For processing DOCX files.
- Pillow - For image processing.
- PyPDF2 - For PDF metadata extraction.

## Installation
To install all required dependencies, you can use the provided requirements.txt file.

``` code
pip install -r requirements.txt
```
## 1. Set File Paths
In the main.ipynb, set the file_path to the location of your PDF or DOCX file:
```code
file_path = '/path/to/your/document.pdf'  # For PDF
# or
file_path = '/path/to/your/document.docx'  # For DOCX
```
## 2. Set Output Directory
The output directory is where extracted content (text, images, links, tables, and metadata) will be saved. Make sure to set the correct path for output_dir in script.py:
```code
output_dir = '/path/to/your/output/directory'
```
##3. Run the Script
You can run the script by using the command:

```code
python script.py
```
The script will process the PDF or DOCX file based on the file extension and perform the following operations:

- Extract text and save it to a .txt file.
- Extract links and save them to a .csv file.
- Extract images and save them to the output directory.
- Extract tables and save them to separate .csv files.
- Extract detailed metadata (fonts, sizes, and text properties) and save it to a .json file.
  


