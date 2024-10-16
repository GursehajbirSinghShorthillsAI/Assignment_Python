import pytest
import os
from unittest.mock import patch, MagicMock
from pdf_loader import PDFLoader  # assuming pdf_loader.py file contains your PDFLoader class
from docx_loader import DOCXLoader  # assuming docx_loader.py contains your DOCXLoader class


# Mock setup for file paths and output directories
@pytest.fixture
def setup_pdf_loader():
    file_path = "sample.pdf"  # Mock file path
    output_dir = "output_pdf"  # Mock output directory
    loader = PDFLoader(file_path, output_dir)
    return loader


@pytest.fixture
def setup_docx_loader():
    file_path = "sample.docx"  # Mock file path
    output_dir = "output_docx"  # Mock output directory
    loader = DOCXLoader(file_path)
    return loader


# Test loading PDF file
def test_pdf_load_file(setup_pdf_loader):
    with patch("fitz.open") as mock_open:
        setup_pdf_loader.load_file()
        mock_open.assert_called_once_with("sample.pdf")


# Test extracting text from PDF
def test_pdf_extract_text(setup_pdf_loader):
    mock_doc = MagicMock()
    mock_doc.load_page.return_value.get_text.return_value = "Sample text"
    setup_pdf_loader.doc = mock_doc

    with patch("builtins.open", mock_open=True) as mock_file:
        setup_pdf_loader.extract_text()
        mock_file.assert_called_once_with(os.path.join("output_pdf", 'text', 'extracted_text.txt'), "w", encoding="utf-8")


# Test extracting links from PDF
def test_pdf_extract_links(setup_pdf_loader):
    mock_doc = MagicMock()
    mock_doc.load_page.return_value.get_links.return_value = [{"uri": "https://example.com"}]
    setup_pdf_loader.doc = mock_doc

    links = setup_pdf_loader.extract_links()
    assert len(links) == 1
    assert links[0]["uri"] == "https://example.com"


# Test extracting images from PDF
def test_pdf_extract_images(setup_pdf_loader):
    mock_doc = MagicMock()
    mock_doc.load_page.return_value.get_images.return_value = [(1, 0, 0, 0, 0, 'image', None, None)]
    setup_pdf_loader.doc = mock_doc

    images = setup_pdf_loader.extract_images()
    assert len(images) > 0


# Test extracting tables from PDF
def test_pdf_extract_tables(setup_pdf_loader):
    mock_doc = MagicMock()
    mock_doc.load_page.return_value.get_text.return_value = "This is a table"
    setup_pdf_loader.doc = mock_doc

    tables = setup_pdf_loader.extract_tables()
    assert len(tables) > 0
    assert "table" in tables[0]["content"].lower()


# Test extracting detailed metadata from PDF
def test_pdf_extract_detailed_metadata(setup_pdf_loader):
    mock_doc = MagicMock()
    mock_doc.load_page.return_value.get_text.return_value = {"blocks": [{"type": 0, "lines": [{"spans": [{"font": "Arial", "size": 12, "text": "Sample text"}]}]}]}
    setup_pdf_loader.doc = mock_doc

    metadata = setup_pdf_loader.extract_detailed_metadata()
    assert len(metadata) > 0
    assert "Arial" in metadata[0]["fonts"][0]["font"]


# Test loading DOCX file
def test_docx_load_file(setup_docx_loader):
    assert setup_docx_loader.doc is not None


# Test extracting text from DOCX
def test_docx_extract_text(setup_docx_loader):
    setup_docx_loader.doc.paragraphs = [MagicMock(text="Sample paragraph")]
    text = setup_docx_loader.extract_text()
    assert "Sample paragraph" in text


# Test extracting links from DOCX
def test_docx_extract_links(setup_docx_loader):
    mock_part = MagicMock()
    mock_part.rels = {"rId1": MagicMock(target_ref="hyperlink")}
    setup_docx_loader.doc.part = mock_part

    links = setup_docx_loader.extract_links()
    assert len(links) == 1
    assert "hyperlink" in links[0]


# Test extracting images from DOCX
def test_docx_extract_images(setup_docx_loader):
    mock_part = MagicMock()
    mock_part.rels = {"rId1": MagicMock(target_ref="image1.png")}
    setup_docx_loader.doc.part = mock_part

    images = setup_docx_loader.extract_images()
    assert len(images) > 0


# Test extracting tables from DOCX
def test_docx_extract_tables(setup_docx_loader):
    mock_table = MagicMock()
    mock_table.rows = [MagicMock(cells=[MagicMock(text="Cell 1"), MagicMock(text="Cell 2")])]
    setup_docx_loader.doc.tables = [mock_table]

    tables = setup_docx_loader.extract_tables()
    assert len(tables) > 0
    assert tables[0][0] == "Cell 1"


# Test extracting detailed metadata from DOCX
def test_docx_extract_detailed_metadata(setup_docx_loader):
    mock_para = MagicMock(text="Sample paragraph")
    mock_run = MagicMock(text="Sample run", font=MagicMock(name="Arial", size=12), bold=True, italic=False, underline=True)
    mock_para.runs = [mock_run]
    setup_docx_loader.doc.paragraphs = [mock_para]

    metadata = setup_docx_loader.extract_detailed_metadata()
    assert len(metadata) > 0
    assert metadata[0]["run_metadata"][0]["font"] == "Arial"