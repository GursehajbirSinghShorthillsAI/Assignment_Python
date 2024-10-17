from abc import ABC, abstractmethod

class Storage(ABC):

    @abstractmethod
    def store_text(self, text_data):
        pass

    @abstractmethod
    def store_links(self, links_data):
        pass

    @abstractmethod
    def store_images(self, images_data):
        pass

    @abstractmethod
    def store_tables(self, tables_data):
        pass