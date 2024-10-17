import os
import sys
from docx import Document
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from loaders.file_loader import AbstractFileLoader
import logging


class DOCXLoader(AbstractFileLoader):
    """
    Concrete implementation of FileLoader for handling DOCX files.
    """

    def check_file(self, filepath):
        """
        Validates that the specified file path ends with '.docx'.

        Args:
        filepath (str): The path to the file to validate.

        Raises:
        ValueError: If the file extension is not .docx.
        """
        if not filepath.lower().endswith('.docx'):
            logging.error(f"Invalid file format for DOCX loader: {filepath}")
            sys.exit(f"Stopping the process due to invalid file format for DOCX loader: {filepath}")
        print(f"Validated DOCX file: {filepath}")
    
    def open_file(self, filepath):
        """
        Loads a DOCX file and returns a Document object.

        Args:
        filepath (str): The path to the file to load.

        Raises:
        IOError: If the file cannot be opened or read.
        """
        try:
            self.check_file(filepath)
            doc = Document(filepath)
            print(f"Loaded DOCX file: {filepath}")
            return doc
        except Exception as e:
            logging.error(f"Unable to open or read the DOCX file due to corruption or other issues: {e}")
            sys.exit(f"Stopping the process due to a critical error with the file: {filepath}")