from abc import ABC, abstractmethod

class Storage(ABC):
    """
    Abstract base class (ABC) that defines a common interface for various storage strategies.
    Concrete implementations must provide methods to store text, links, images, and tables.
    
    This ensures that all types of data extracted from documents are handled consistently
    across different storage implementations.
    """

    @abstractmethod
    def store_text(self, text_data):
        """
        Abstract method to store extracted text data.
        
        Args:
            text_data (str): The text data to be stored.
        
        Implementations should define how text data is persisted, e.g., to a file, database, etc.
        """
        pass

    @abstractmethod
    def store_links(self, links_data):
        """
        Abstract method to store extracted hyperlink data.
        
        Args:
            links_data (list): A list of dictionaries where each dictionary contains details of a hyperlink.
        
        Implementations should define how hyperlink data is persisted, such as in a database or JSON file.
        """
        pass

    @abstractmethod
    def store_images(self, images_data):
        """
        Abstract method to store extracted image data.
        
        Args:
            images_data (list): A list of image data, typically including metadata such as image format, source, etc.
        
        Implementations should define how images are stored, potentially as files on disk with metadata stored separately.
        """
        pass

    @abstractmethod
    def store_tables(self, tables_data):
        """
        Abstract method to store extracted table data.
        
        Args:
            tables_data (list): A list of table data, which might be represented as lists of lists or other structured formats.
        
        Implementations should define how tables are stored, such as in CSV files, databases, or other structured formats.
        """
        pass