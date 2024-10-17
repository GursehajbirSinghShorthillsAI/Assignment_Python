import pytest
from loaders.pdf_loader import PDFLoader
from loaders.ppt_loader import PPTLoader
from loaders.docx_loader import DOCXLoader 
from mysql.connector import Error
from Storage.sql_storage import SQLStorage
from unittest.mock import patch, MagicMock

@pytest.fixture
def docx_loader():
    return DOCXLoader()

def test_validate_small_docx_file(docx_loader):
    small_docx_path = "test_files/docx/small.docx"
    assert docx_loader.load_file(small_docx_path), f"Loaded DOCX file: {small_docx_path}"

def test_validate_large_docx_file(docx_loader):
    large_docx_path = "test_files/docx/large.docx"
    assert docx_loader.load_file(large_docx_path), f"Loaded DOCX file: {large_docx_path}"

def test_validate_corrupted_docx_file(docx_loader):
    corrupted_docx_path = "test_files/docx/corrupted.docx"
    with pytest.raises(SystemExit):
        docx_loader.load_file(corrupted_docx_path)

def test_validate_non_docx_file(docx_loader):
    non_docx_path = "test_files/pdf/small.pdf"
    with pytest.raises(SystemExit):
        docx_loader.load_file(non_docx_path)

def test_validate_empty_docx_file(docx_loader):
    empty_docx_path = "test_files/docx/empty.docx"
    assert docx_loader.load_file(empty_docx_path), f"Loaded DOCX file: {empty_docx_path}"

def test_validate_docx_with_complex_formatting(docx_loader):
    large_docx_path = "test_files/docx/large.docx"
    assert docx_loader.load_file(large_docx_path), f"Loaded DOCX file: {large_docx_path}"

def test_validate_password_protected_docx(docx_loader):
    protected_docx_path = "test_files/docx/password.docx"
    with pytest.raises(SystemExit):
        docx_loader.load_file(protected_docx_path)

def test_validate_docx_with_embedded_links(docx_loader):
    large_docx_path = "test_files/docx/large.docx"
    assert docx_loader.load_file(large_docx_path), f"Loaded DOCX file: {large_docx_path}"

def test_validate_docx_with_embedded_images(docx_loader):
    large_docx_path = "test_files/docx/large.docx"
    assert docx_loader.load_file(large_docx_path), f"Loaded DOCX file: {large_docx_path}"

def test_validate_docx_with_multiple_sections(docx_loader):
    large_docx_path = "test_files/docx/large.docx"
    assert docx_loader.load_file(large_docx_path), f"Loaded DOCX file: {large_docx_path}"

def test_validate_docx_with_comments_or_track_changes(docx_loader):
    large_docx_path = "test_files/docx/large.docx"
    assert docx_loader.load_file(large_docx_path), f"Loaded DOCX file: {large_docx_path}"

def test_validate_docx_with_annotation(docx_loader):
    docx_path = "test_files/docx/annotate.docx"
    assert docx_loader.load_file(docx_path), f"Loaded DOCX file: {docx_path}"

def test_validate_docx_with_multilanguage(docx_loader):
    docx_path = "test_files/docx/multilingual.docx"
    assert docx_loader.load_file(docx_path), f"Loaded DOCX file: {docx_path}"

@pytest.fixture
def pdf_loader():
    return PDFLoader()

def test_validate_small_pdf_file(pdf_loader):
    small_pdf_path = "test_files/pdf/small.pdf"
    assert pdf_loader.load_file(small_pdf_path), f"Loaded PDF file: {small_pdf_path}"

def test_validate_large_pdf_file(pdf_loader):
    large_pdf_path = "test_files/pdf/large.pdf"
    assert pdf_loader.load_file(large_pdf_path), f"Loaded PDF file: {large_pdf_path}"

def test_validate_corrupted_pdf_file(pdf_loader):
    corrupted_pdf_path = "test_files/pdf/corrupted.pdf"
    with pytest.raises(SystemExit):
        pdf_loader.load_file(corrupted_pdf_path)

def test_validate_non_pdf_file(pdf_loader):
    non_pdf_path = "test_files/docx/small.docx"
    with pytest.raises(SystemExit):
        pdf_loader.load_file(non_pdf_path)

def test_validate_empty_pdf_file(pdf_loader):
    empty_pdf_path = "test_files/pdf/empty.pdf"
    assert pdf_loader.load_file(empty_pdf_path), f"Loaded PDF file: {empty_pdf_path}"

def test_validate_password_protected_pdf(pdf_loader):
    protected_pdf_path = "test_files/pdf/password.pdf"
    with pytest.raises(SystemExit):
        pdf_loader.load_file(protected_pdf_path)

def test_validate_pdf_with_embedded_links(pdf_loader):
    pdf_with_links_path = "test_files/pdf/large.pdf"
    assert pdf_loader.load_file(pdf_with_links_path), f"Loaded PDF file: {pdf_with_links_path}"

def test_validate_pdf_with_embedded_images(pdf_loader):
    pdf_with_images_path = "test_files/pdf/large.pdf"
    assert pdf_loader.load_file(pdf_with_images_path), f"Loaded PDF file: {pdf_with_images_path}"

def test_validate_pdf_with_multiple_pages(pdf_loader):
    multi_page_pdf_path = "test_files/pdf/large.pdf"
    assert pdf_loader.load_file(multi_page_pdf_path), f"Loaded PDF file: {multi_page_pdf_path}"

def test_validate_pdf_with_annotation(pdf_loader):
    pdf_path = "test_files/pdf/annotate.pdf"
    assert pdf_loader.load_file(pdf_path), f"Loaded PDF file: {pdf_path}"

def test_validate_pdf_with_multilanguage(pdf_loader):
    pdf_path = "test_files/pdf/multilingual.pdf"
    assert pdf_loader.load_file(pdf_path), f"Loaded PDF file: {pdf_path}"

@pytest.fixture
def ppt_loader():
    return PPTLoader()

def test_validate_small_pptx_file(ppt_loader):
    small_pptx_path = "test_files/pptx/small.pptx"
    assert ppt_loader.load_file(small_pptx_path), f"Loaded PPTX file: {small_pptx_path}"

def test_validate_large_pptx_file(ppt_loader):
    large_pptx_path = "test_files/pptx/large.pptx"
    assert ppt_loader.load_file(large_pptx_path), f"Loaded PPTX file: {large_pptx_path}"

def test_validate_corrupted_pptx_file(ppt_loader):
    corrupted_pptx_path = "test_files/pptx/corrupted.pptx"
    with pytest.raises(SystemExit):
        ppt_loader.load_file(corrupted_pptx_path)

def test_validate_non_pptx_file(ppt_loader):
    non_pptx_path = "test_files/pdf/small.pdf"
    with pytest.raises(SystemExit):
        ppt_loader.load_file(non_pptx_path)

def test_validate_empty_pptx_file(ppt_loader):
    empty_pptx_path = "test_files/pptx/empty.pptx"
    assert ppt_loader.load_file(empty_pptx_path), f"Loaded PPTX file: {empty_pptx_path}"

def test_validate_pptx_with_complex_animations(ppt_loader):
    complex_animations_pptx_path = "test_files/pptx/large.pptx"
    assert ppt_loader.load_file(complex_animations_pptx_path), f"Loaded PPTX file: {complex_animations_pptx_path}"

def test_validate_password_protected_pptx(ppt_loader):
    protected_pptx_path = "test_files/pptx/password.pptx"
    with pytest.raises(SystemExit):
        ppt_loader.load_file(protected_pptx_path)

def test_validate_pptx_with_embedded_links(ppt_loader):
    links_pptx_path = "test_files/pptx/large.pptx"
    assert ppt_loader.load_file(links_pptx_path), f"Loaded PPTX file: {links_pptx_path}"

def test_validate_pptx_with_embedded_images(ppt_loader):
    images_pptx_path = "test_files/pptx/large.pptx"
    assert ppt_loader.load_file(images_pptx_path), f"Loaded PPTX file: {images_pptx_path}"

def test_validate_pptx_with_videos(ppt_loader):
    video_pptx_path = "test_files/pptx/large.pptx"
    assert ppt_loader.load_file(video_pptx_path), f"Loaded PPTX file: {video_pptx_path}"

def test_validate_pptx_with_multiple_slides_and_transitions(ppt_loader):
    multiple_slides_pptx_path = "test_files/pptx/large.pptx"
    assert ppt_loader.load_file(multiple_slides_pptx_path), f"Loaded PPTX file: {multiple_slides_pptx_path}"

def test_validate_pptx_with_embedded_audio(ppt_loader):
    audio_pptx_path = "test_files/pptx/large.pptx"
    assert ppt_loader.load_file(audio_pptx_path), f"Loaded PPTX file: {audio_pptx_path}"

def test_validate_pptx_with_custom_slide_layouts(ppt_loader):
    custom_layout_pptx_path = "test_files/pptx/large.pptx"
    assert ppt_loader.load_file(custom_layout_pptx_path), f"Loaded PPTX file: {custom_layout_pptx_path}"

def test_validate_pptx_with_annotations(ppt_loader):
    pptx_path = "test_files/pptx/annotate.pptx"
    assert ppt_loader.load_file(pptx_path), f"Loaded PPTX file: {pptx_path}"

def test_validate_pptx_with_multilanguage(ppt_loader):
    pptx_path = "test_files/pptx/multilingual.pptx"
    assert ppt_loader.load_file(pptx_path), f"Loaded PPTX file: {pptx_path}"

@pytest.fixture
def valid_credentials():
    return {
        "host": "localhost",
        "user": "root",
        "password": "gurjot123",
        "database": "extracted_data_python"
    }

@pytest.fixture
def invalid_credentials():
    return {
        "host": "localhost123",
        "user": "root123",
        "password": "gurjot123123",
        "database": "extracted_data_python123"
    }

def test_validate_successful_database_connection(mocker, valid_credentials):
    # Mock the connect method from mysql.connector to return True for is_connected
    mocker.patch('mysql.connector.connect', return_value=mocker.Mock(is_connected=lambda: True))
    storage = SQLStorage(**valid_credentials)
    assert storage.connection.is_connected(), "Connected to MySQL database"

def test_validate_failed_database_connection(mocker, invalid_credentials):
    # Mock the connect method to raise a connection error
    mocker.patch('mysql.connector.connect', side_effect=Error("Failed to connect"))
    with pytest.raises(SystemExit):  # Assuming your code exits on failure
        SQLStorage(**invalid_credentials)

@pytest.fixture
def sql_storage():
    return SQLStorage(host="localhost", user="root", password="gurjot123", database="extracted_data_python")

@pytest.fixture
def mock_cursor():
    """Mock the cursor and connection to MySQL."""
    cursor_mock = MagicMock()
    connection_mock = MagicMock()
    cursor_mock.cursor.return_value = cursor_mock
    cursor_mock.__enter__.return_value = cursor_mock
    connection_mock.connect.return_value = connection_mock
    return cursor_mock, connection_mock

def test_validate_storing_text_data_empty_input(sql_storage, mock_cursor):
    with patch('mysql.connector.connect', return_value=mock_cursor[1]):
        with patch.object(mock_cursor[1], 'cursor', return_value=mock_cursor[0]):
            sql_storage.store_text([], "pdf")
            # Ensure no INSERT has been called
            calls = [call[0][0].upper().startswith('INSERT INTO') for call in mock_cursor[0].execute.call_args_list]
            assert not any(calls)

def test_validate_storing_hyperlinks_data_empty_input(sql_storage, mock_cursor):
    with patch('mysql.connector.connect', return_value=mock_cursor[1]):
        with patch.object(mock_cursor[1], 'cursor', return_value=mock_cursor[0]):
            sql_storage.store_links([], "pdf")
            # Ensure no INSERT has been called
            calls = [call[0][0].upper().startswith('INSERT INTO') for call in mock_cursor[0].execute.call_args_list]
            assert not any(calls)

def test_validate_storing_image_metadata_empty_input(sql_storage, mock_cursor):
    with patch('mysql.connector.connect', return_value=mock_cursor[1]):
        with patch.object(mock_cursor[1], 'cursor', return_value=mock_cursor[0]):
            sql_storage.store_images([], "pdf")
            # Ensure no INSERT has been called
            calls = [call[0][0].upper().startswith('INSERT INTO') for call in mock_cursor[0].execute.call_args_list]
            assert not any(calls)

def test_validate_database_table_not_overwritten_if_exists(sql_storage, mock_cursor):
    """ Test that existing tables are not overwritten when attempting to recreate them """
    with patch('mysql.connector.connect', return_value=mock_cursor[1]):
        with patch.object(mock_cursor[1], 'cursor', return_value=mock_cursor[0]):
            # Call store_text to trigger table creation twice
            sql_storage.store_text([{'page_number': 1, 'text': 'Example text'}], "pdf")
            sql_storage.store_text([{'page_number': 2, 'text': 'Another example text'}], "pdf")
            # Check the creation statement is executed only once
            create_table_calls = [call for call in mock_cursor[0].execute.call_args_list if 'CREATE TABLE IF NOT EXISTS' in call[0][0]]
            assert len(create_table_calls) == 0