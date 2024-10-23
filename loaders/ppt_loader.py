import os
import sys
from file_loader import FileLoader
from pptx import Presentation
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sys

class PPTLoader(FileLoader):
    file_extension = '.pptx'

    def load_file(self, filepath: str):
        if self.check_file(filepath):  # Utilizes the inherited validate_file method to check file extension.
            try:
                ppt = Presentation(filepath)  # Attempts to open and read the PPTX file.
                print(f"Loaded PPTX file: {filepath}")
                return ppt
            except Exception as e:
                logging.error(f"Unable to open or read the PPT file: {e}")
                sys.exit(f"Stopping the process due to a critical error with the PPT file: {filepath}")