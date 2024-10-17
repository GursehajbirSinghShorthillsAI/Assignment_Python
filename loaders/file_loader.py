from abc import ABC, abstractmethod

class AbstractFileLoader(ABC):

    @abstractmethod
    def check_file(self, file_path: str) -> bool:
        pass

    @abstractmethod
    def open_file(self, file_path: str):
        pass
