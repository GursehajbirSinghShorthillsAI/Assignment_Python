import os
import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Storage.sql_storage import SQLStorage
from loaders.pdf_loader import PDFLoader
from loaders.ppt_loader import PPTLoader
from loaders.docx_loader import DOCXLoader
from data_extractor1 import DataExtractor
from dotenv import load_dotenv

load_dotenv("config.env")  # Load environment variables from 'config.env'

def ensure_directory(path):
    """
    Creates the directory if it does not exist.
    Args:
        path (str): Path to the directory to be ensured.
    """
    if not os.path.exists(path):
        os.makedirs(path)  # Make directory if it does not exist.

def save_to_file(data, filename):
    """
    Serializes data to a JSON file.
    Args:
        data: Data to be serialized.
        filename (str): Path to the output JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)  # Write data as pretty-printed JSON.

def main():
    # Retrieve database credentials from environment variables
    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")

    # Create the base directory structure for outputs
    base_output_folder = "output"
    ensure_directory(base_output_folder)  # Ensure the base output directory exists

    # Define subdirectories for each type of content
    text_output_folder = os.path.join(base_output_folder, "text")
    links_output_folder = os.path.join(base_output_folder, "links")
    images_output_folder = os.path.join(base_output_folder, "images")
    tables_output_folder = os.path.join(base_output_folder, "tables")

    # Ensure subdirectories for each file format within each content type
    for category in [text_output_folder, links_output_folder, images_output_folder, tables_output_folder]:
        ensure_directory(os.path.join(category, "pdf"))
        ensure_directory(os.path.join(category, "docx"))
        ensure_directory(os.path.join(category, "pptx"))

    
    pdf_loader = PDFLoader()   
    docx_loader = DOCXLoader() 
    ppt_loader = PPTLoader()   

    # Set the file paths for each loader to specify which files they will process.
    pdf_loader.filepath = "Sample_file/sample.pdf"   # Path to the PDF file to be processed.
    docx_loader.filepath = "Sample_file/sample.docx" # Path to the DOCX file to be processed.
    ppt_loader.filepath = "" # Path to the PPTX file to be processed.


    # -------------------- Text Extraction --------------------
    # Initialize a DataExtractor for PDF files using the previously set up PDFLoader.
    pdf_text_extractor = DataExtractor(pdf_loader)
    # Extract text from the specified PDF file.
    pdf_text = pdf_text_extractor.extract_text()
    # Save the extracted text data to a JSON file in the designated output folder for PDF text.
    save_to_file(pdf_text, os.path.join(text_output_folder, "pdf", "pdf_text.json"))

    # Initialize a DataExtractor for DOCX files using the DOCXLoader.
    docx_text_extractor = DataExtractor(docx_loader)
    # Extract text from the specified DOCX file.
    docx_text = docx_text_extractor.extract_text()
    # Save the extracted text data to a JSON file in the designated output folder for DOCX text.
    save_to_file(docx_text, os.path.join(text_output_folder, "docx", "docx_text.json"))

    # Initialize a DataExtractor for PPTX files using the PPTLoader.
    ppt_text_extractor = DataExtractor(ppt_loader)
    # Extract text from the specified PPTX file.
    ppt_text = ppt_text_extractor.extract_text()
    # Save the extracted text data to a JSON file in the designated output folder for PPTX text.
    save_to_file(ppt_text, os.path.join(text_output_folder, "pptx", "pptx_text.json"))


    # -------------------- Link Extraction --------------------
    # Initialize a DataExtractor for PDF files to handle hyperlink extraction.
    pdf_link_extractor = DataExtractor(pdf_loader)
    # Extract hyperlinks from the specified PDF file.
    pdf_links = pdf_link_extractor.extract_links()
    # Save the extracted hyperlink data to a JSON file in the designated output folder for PDF links.
    save_to_file(pdf_links, os.path.join(links_output_folder, "pdf", "pdf_links.json"))

    # Initialize a DataExtractor for DOCX files to handle hyperlink extraction.
    docx_link_extractor = DataExtractor(docx_loader)
    # Extract hyperlinks from the specified DOCX file.
    docx_links = docx_link_extractor.extract_links()
    # Save the extracted hyperlink data to a JSON file in the designated output folder for DOCX links.
    save_to_file(docx_links, os.path.join(links_output_folder, "docx", "docx_links.json"))

    # Initialize a DataExtractor for PPTX files to handle hyperlink extraction.
    ppt_link_extractor = DataExtractor(ppt_loader)
    # Extract hyperlinks from the specified PPTX file.
    ppt_links = ppt_link_extractor.extract_links()
    # Save the extracted hyperlink data to a JSON file in the designated output folder for PPTX links.
    save_to_file(ppt_links, os.path.join(links_output_folder, "pptx", "pptx_links.json"))


    # -------------------- Image Extraction --------------------
    # Initialize a DataExtractor for PDF files to handle image extraction.
    pdf_image_extractor = DataExtractor(pdf_loader)
    # Extract images from the specified PDF file.
    pdf_images = pdf_image_extractor.extract_images()
    # Save the extracted image data to a JSON file in the designated output folder for PDF images.
    save_to_file(pdf_images, os.path.join(images_output_folder, "pdf", "pdf_images.json"))

    # Initialize a DataExtractor for DOCX files to handle image extraction.
    docx_image_extractor = DataExtractor(docx_loader)
    # Extract images from the specified DOCX file.
    docx_images = docx_image_extractor.extract_images()
    # Save the extracted image data to a JSON file in the designated output folder for DOCX images.
    save_to_file(docx_images, os.path.join(images_output_folder, "docx", "docx_images.json"))

    # Initialize a DataExtractor for PPTX files to handle image extraction.
    ppt_image_extractor = DataExtractor(ppt_loader)
    # Extract images from the specified PPTX file.
    ppt_images = ppt_image_extractor.extract_images()
    # Save the extracted image data to a JSON file in the designated output folder for PPTX images.
    save_to_file(ppt_images, os.path.join(images_output_folder, "pptx", "pptx_images.json"))


    # -------------------- Table Extraction --------------------
    # Initialize a DataExtractor for PDF files specifically for extracting tables.
    pdf_table_extractor = DataExtractor(pdf_loader)
    # Extract tables from the specified PDF file and store the result.
    pdf_tables = pdf_table_extractor.extract_tables()

    # Initialize a DataExtractor for DOCX files specifically for extracting tables.
    docx_table_extractor = DataExtractor(docx_loader)
    # Extract tables from the specified DOCX file and store the result.
    docx_tables = docx_table_extractor.extract_tables()

    # Initialize a DataExtractor for PPTX files specifically for extracting tables.
    ppt_table_extractor = DataExtractor(ppt_loader)
    # Extract tables from the specified PPTX file and store the result.
    ppt_tables = ppt_table_extractor.extract_tables()


    # Setup SQLStorage using the credentials from environment variables
    # Adjust these credentials according to your MySQL setup.
    storage = SQLStorage(host=db_host, user=db_user, password=db_password, database=db_name)
    # Check if the connection to the MySQL database is successful
    if storage.connection.is_connected():
        print("Successfully connected to the MySQL database")
    else:
        print("Failed to connect to the MySQL database")

    # Extract and store data for PDF
    pdf_extractor = DataExtractor(pdf_loader)  # Initialize a DataExtractor for PDF files.
    storage.store_text(pdf_extractor.extract_text(), "pdf")  # Extract text from the PDF and store it in the database under the "pdf" category.
    storage.store_links(pdf_extractor.extract_links(), "pdf")  # Extract hyperlinks from the PDF and store them in the database under the "pdf" category.
    storage.store_images(pdf_extractor.extract_images(), "pdf")  # Extract images from the PDF and store them in the database under the "pdf" category.
    storage.store_tables(pdf_extractor.extract_tables(), "pdf")  # Extract tables from the PDF and store them in the database under the "pdf" category.

    # Extract and store data for DOCX
    docx_extractor = DataExtractor(docx_loader)  # Initialize a DataExtractor for DOCX files.
    storage.store_text(docx_extractor.extract_text(), "docx")  # Extract text from the DOCX and store it in the database under the "docx" category.
    storage.store_links(docx_extractor.extract_links(), "docx")  # Extract hyperlinks from the DOCX and store them in the database under the "docx" category.
    storage.store_images(docx_extractor.extract_images(), "docx")  # Extract images from the DOCX and store them in the database under the "docx" category.
    storage.store_tables(docx_extractor.extract_tables(), "docx")  # Extract tables from the DOCX and store them in the database under the "docx" category.

    # Extract and store data for PPTX
    ppt_extractor = DataExtractor(ppt_loader)  # Initialize a DataExtractor for PPTX files.
    storage.store_text(ppt_extractor.extract_text(), "pptx")  # Extract text from the PPTX and store it in the database under the "pptx" category.
    storage.store_links(ppt_extractor.extract_links(), "pptx")  # Extract hyperlinks from the PPTX and store them in the database under the "pptx" category.
    storage.store_images(ppt_extractor.extract_images(), "pptx")  # Extract images from the PPTX and store them in the database under the "pptx" category.
    storage.store_tables(ppt_extractor.extract_tables(), "pptx")  # Extract tables from the PPTX and store them in the database under the "pptx" category.

if __name__ == "__main__":
    main()