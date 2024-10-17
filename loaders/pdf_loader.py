import sys
from PyPDF2 import PdfReader

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from loaders.file_loader import AbstractFileLoader

class PDFLoader(AbstractFileLoader):
    """
    A class to load PDF files, ensuring they meet basic format requirements.
    Extends the FileLoader abstract base class to handle PDF-specific loading operations.
    """

    def check_file(self, filepath):
        """
        Validates that the specified file path ends with '.pdf' to ensure it's a PDF file.
        
        Args:
            filepath (str): The path to the file that needs validation.
        
        Raises:
            ValueError: If the file extension is not .pdf.
        """
        # Check if the file's extension is '.pdf'
        if not filepath.lower().endswith('.pdf'):
            sys.exit(f"Invalid file format. Expected a PDF file.")
            raise ValueError("Invalid file format. Expected a PDF file.")
        print(f"Validated PDF file: {filepath}")

    def open_file(self, filepath):
        """
        Loads the PDF file and returns a PdfReader object that allows further manipulation
        and data extraction from the PDF.
        
        Args:
            filepath (str): The path to the file that needs to be loaded.
        
        Returns:
            PdfReader: An object that represents the opened PDF file.
        """
        # Validate the file to ensure it is a PDF
        try:
            self.check_file(filepath)
            reader = PdfReader(filepath)
            print(f"Loaded PDF file: {filepath}")
            return reader
            # Return the PdfReader object for potential further processing outside this method
        except:
            sys.exit(f"Unable to open or read the PDF file due to corruption or other issues")