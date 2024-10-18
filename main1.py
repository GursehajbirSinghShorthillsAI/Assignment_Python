import os
import json
import sys
from widget import upload_file
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
    db_user = os.getenv("DB_USERNAME")
    db_password = os.getenv("PASSWORD")
    db_name = os.getenv("DATABASE")
    # Create the base directory structure for outputs
    base_output_folder = "output"
    ensure_directory(base_output_folder)  # Ensure the base output directory exists

    # Define subdirectories for each type of content
    output_folders = {
        "text": os.path.join(base_output_folder, "text"),
        "links": os.path.join(base_output_folder, "links"),
        "images": os.path.join(base_output_folder, "images"),
        "tables": os.path.join(base_output_folder, "tables")
    }

    # Ensure subdirectories for each file format within each content type
    for category, folder in output_folders.items():
        ensure_directory(os.path.join(folder, "pdf"))
    
    file_path = upload_file()
    if file_path:
        # Process the uploaded file as needed
        print(f"Processing file: {file_path}")
    else:
        print("No file to process.")
    #file_path = 'Sample_file/sample.pdf'

    loader = None
    file_format = None

    if file_path.endswith(".pdf"):
        loader = PDFLoader()
        file_format = "pdf"
    elif file_path.endswith(".docx"):
        loader = DOCXLoader()
        file_format = "docx"
    elif file_path.endswith(".pptx"):
        loader = PPTLoader()
        file_format = "pptx"
    else:
        print(f"Unsupported file format for {file_path}")
        return

    if loader is None:
        print(f"Loader for file {file_path} could not be determined.")
        return
    
    loader.filepath = file_path



    extractor = DataExtractor(loader)

    extracted_text = extractor.extract_text()
    if extracted_text:
        save_to_file(extracted_text, os.path.join(output_folders["text"], file_format, f"{file_format}_text.json"))

    # Define a list of tasks for each content type: links, images, and tables
    tasks = [
        ("links", "extract_links", "links"),
        ("images", "extract_images", "images"),
        ("tables", "extract_tables", None)  # No need for output folder for tables as it stores directly in DB
    ]

    # Loop through each task (links, images, tables) for each file format (PDF, DOCX, PPTX)
    for category, extract_method, output_type in tasks:
        extracted_data = getattr(extractor, extract_method)()  # Dynamically call the extraction method
        
        if extracted_data: 
            # If the task is to store in a file (for links and images), save to the appropriate output folder
            if output_type:
                output_path = os.path.join(output_folders[output_type], file_format, f"{file_format}_{category}.json")
                save_to_file(extracted_data, output_path)
                print(f"{category.capitalize()} extraction completed and saved.")
        else:
            print(f"No {category} data extracted.")
                

    # Setup SQLStorage using the credentials from environment variables
    storage = SQLStorage(host=db_host, user=db_user, password=db_password, database=db_name)

    # Check if the connection to the MySQL database is successful
    if storage.connection.is_connected():
        print("Successfully connected to the MySQL database")
    else:
        print("Failed to connect to the MySQL database")

    # Store data in the database for each content type
    for category, extract_method, _ in tasks + [("text", "extract_text", "text")]:
            extracted_data = getattr(extractor, extract_method)()
            getattr(storage, f"store_{category}")(extracted_data, file_format)  # Dynamically store data in the DB
            if extracted_data:
                getattr(storage, f"store_{category}")(extracted_data, "pdf")
                print(f"{category.capitalize()} data stored in the database.")
            else:
                print(f"No {category} data to store in the database.")



# Helper functions (ensure_directory, save_to_file, etc.) should be defined as required
if __name__ == "__main__":
    main()