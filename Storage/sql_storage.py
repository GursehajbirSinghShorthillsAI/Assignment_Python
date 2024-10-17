import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from .storage import Storage
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
load_dotenv()

class SQLStorage(Storage):

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self._connect()

    def _connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            sys.exit(1)

    def _execute_query(self, query, data=None):

        cursor = self.connection.cursor()
        try:
            cursor.execute(query, data)
            self.connection.commit()
        except Error as e:
            print(f"Error executing query: {e}")
        finally:
            cursor.close()

    def store_text(self, text_data, file_type):
        """
        Stores extracted text data into a MySQL database.
        Args:
            text_data (list of dicts): The text data to store, each item contains page number and text content.
            file_type (str): The type of file from which the text is extracted.
        """
        query = """
        CREATE TABLE IF NOT EXISTS text_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            file_type VARCHAR(255),
            page_number INT,
            text TEXT
        );
        """
        self._execute_query(query)

        insert_query = "INSERT INTO text_data (file_type, page_number, text) VALUES (%s, %s, %s)"
        for item in text_data:
            self._execute_query(insert_query, (file_type, item.get('page_number'), item.get('text')))
        print(f"Text data inserted into the database for {file_type}.")
    
    def store_links(self, links_data, file_type):
        """
        Stores extracted hyperlink data into the MySQL database.
        This includes creating a table for links if it does not already exist and inserting the hyperlink data.

        Args:
            links_data (list of dicts): The hyperlink data to store, each item contains page number, linked text, and the hyperlink.
            file_type (str): The type of file from which the links are extracted.

        Each link is stored with its file type, page number, the text of the link, and the URL.
        """
        query = """
        CREATE TABLE IF NOT EXISTS links_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            file_type VARCHAR(255),
            page_number INT,
            linked_text TEXT,
            link TEXT
        );
        """
        self._execute_query(query)

        insert_query = "INSERT INTO links_data (file_type, page_number, linked_text, link) VALUES (%s, %s, %s, %s)"
        for item in links_data:
            self._execute_query(insert_query, (file_type, item.get('page_number'), item.get('linked_text'), item.get('link')))
        print(f"Links data inserted into the database for {file_type}.")

    def store_images(self, images_data, file_type):
        """
        Stores extracted image metadata into the MySQL database.
        This involves creating a table for images if it does not exist and inserting metadata about each image.

        Args:
            images_data (list of dicts): The image data to store, each item contains page number, image filename, and image format.
            file_type (str): The type of file from which the images are extracted.

        Each image's metadata includes the file type, page number, filename, and format.
        """
        query = """
        CREATE TABLE IF NOT EXISTS images_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            file_type VARCHAR(255),
            page_number INT,
            image_filename VARCHAR(255),
            image_format VARCHAR(50)
        );
        """
        self._execute_query(query)

        insert_query = "INSERT INTO images_data (file_type, page_number, image_filename, image_format) VALUES (%s, %s, %s, %s)"
        for item in images_data:
            self._execute_query(insert_query, (file_type, item.get('page_number'), item.get('image_filename'), item.get('image_format')))
        print(f"Image data inserted into the database for {file_type}.")

    def store_tables(self, tables_data, file_type):
        """
        Stores extracted tables metadata into the MySQL database.
        This includes creating a table for storing tables data if it does not already exist and inserting the table data.

        Args:
            tables_data (list of dicts): The table data to store, each item contains page number and the filename of the CSV representing the table.
            file_type (str): The type of file from which the tables are extracted.

        Each table's metadata is stored with its file type, page number, and the CSV filename that stores the table's actual data.
        """
        query = """
        CREATE TABLE IF NOT EXISTS tables_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            file_type VARCHAR(255),
            page_number INT,
            csv_filename VARCHAR(255)
        );
        """
        self._execute_query(query)

        insert_query = "INSERT INTO tables_data (file_type, page_number, csv_filename) VALUES (%s, %s, %s)"
        for item in tables_data:
            self._execute_query(insert_query, (file_type, item.get('page_number'), item.get('csv_filename')))
        print(f"Table data inserted into the database for {file_type}.")