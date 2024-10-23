import os
import sys
from file_loader import FileLoader
from PyPDF2 import PdfReader
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class PDFLoader(FileLoader):

    file_extension = '.pdf'

    def load_file(self, filepath: str):

        if self.check_file(filepath):  # Utilizes the validate_file method from the abstract base class.
            try:
                reader = PdfReader(filepath)  # Attempts to open and read the PDF file.
                print(f"Loaded PDF file: {filepath}")
                return reader
            except Exception:
                sys.exit(f"Unable to open or read the PDF file due to corruption or other issues")