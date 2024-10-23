from abc import ABC, abstractmethod
import sys
import logging

class FileLoader(ABC):

    file_extension = ""

    def check_file(self, filepath: str) -> bool:

        if not filepath.lower().endswith(self.file_extension):
            logging.error(f"Invalid file format: {filepath}")
            sys.exit(f"Invalid format stopped process: {filepath}")
        print(f"File validated: {filepath}")
        return True

    @abstractmethod
    def open_file(self, filepath: str):
        raise NotImplementedError("Load method not implemented.")