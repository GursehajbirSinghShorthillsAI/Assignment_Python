# class DataExtractor:
#     def __init__(self, file_path, output_dir):
#         self.file_path = file_path
#         self.output_dir = output_dir
#         self.loader = self._select_loader()

#     def _select_loader(self):
#         """Selects the appropriate loader based on file extension."""
#         if self.file_path.endswith('.pdf'):
#             from pdf_loader import PDFLoader
#             return PDFLoader(self.file_path, self.output_dir)
#         elif self.file_path.endswith('.docx'):
#             from docx_loader import DOCXLoader
#             return DOCXLoader(self.file_path, self.output_dir)
#         elif self.file_path.endswith('.pptx'):
#             from ppt_loader import PPTLoader
#             return PPTLoader(self.file_path, self.output_dir)
#         else:
#             raise ValueError(f"Unsupported file format: {self.file_path}")

#     def extract_text(self):
#         """Extracts text from the file."""
#         self.loader.extract_text()

#     def extract_images(self):
#         """Extracts images from the file."""
#         self.loader.extract_images()

#     def extract_links(self):
#         """Extracts links from the file."""
#         self.loader.extract_links()

#     def extract_tables(self):
#         """Extracts tables from the file."""
#         self.loader.extract_tables()

#     def extract_metadata(self):
#         """Extracts metadata from the file, if applicable."""
#         if hasattr(self.loader, 'extract_detailed_metadata'):
#             self.loader.extract_detailed_metadata()
#         else:
#             print("Metadata extraction not supported for this file type.")

# # Example usage of the DataExtractor class
# if __name__ == "__main__":
#     file_path = 'Sample_file/sample.pptx'  # Change to the file you're processing
#     output_dir = 'output_directory_path'  # Change to the directory where you want to save the output

#     extractor = DataExtractor(file_path, output_dir)

#     # Extract text, images, links, and tables
#     extractor.extract_text()
#     extractor.extract_images()
#     extractor.extract_links()
#     extractor.extract_tables()

#     # Extract metadata (for PDF and DOCX files, metadata extraction supported)
#     extractor.extract_metadata()

#     print("Extraction complete. Check the output directory for results.")