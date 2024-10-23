import os
import sys
from file_loader import FileLoader
from docx import Document
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import logging
import sys

class DOCXLoader(FileLoader):

    file_extension = '.docx'

    def load_file(self, filepath: str):
        if self.check_file_file(filepath):  # Utilizes the validate_file method from the abstract base class.
            try:
                doc = Document(filepath)  # Attempts to open and read the DOCX file.
                print(f"Loaded DOCX file: {filepath}")
                return doc
            except Exception as e:
                logging.error(f"Unable to open or read the DOCX file: {e}")
                sys.exit(f"Stopping the process due to a critical error with the DOCX file: {filepath}")