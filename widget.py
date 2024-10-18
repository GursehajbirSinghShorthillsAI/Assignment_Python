import tkinter as tk
from tkinter import filedialog

def upload_file():
    """Open a file dialog to upload a file from the user's local machine."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select a file")
    if file_path:
        print(f"File uploaded: {file_path}")
        return file_path
    else:
        print("No file selected.")
        return None
    

if __name__ == "__main__":
    file_path = upload_file()
    if file_path:
        # Do something with the file, like pass it to a processing function
        print(f"Processing file: {file_path}")
    else:
        print("No file to process.")