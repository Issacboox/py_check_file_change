import os
import json
from pypdf import PdfReader

def count_pdf_pages(file_path):
    try:
        reader = PdfReader(file_path)
        return len(reader.pages)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0

def scan_folder(base_dir, rel_path="."):
    """
    Recursively scans a folder and returns:
    - folder info (list of dicts)
    - total pages of this folder and all nested folders
    """
    folder_path = os.path.join(base_dir, rel_path)
    folder_pdf_files = []
    total_pages_folder = 0
    folder_data = []

    # Count PDFs directly in this folder
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path) and file.lower().endswith(".pdf"):
            pages = count_pdf_pages(file_path)
            folder_pdf_files.append({"name": file, "pages": pages})
            total_pages_folder += pages

    # Recursively scan subfolders
    for entry in os.listdir(folder_path):
        entry_path = os.path.join(folder_path, entry)
        if os.path.isdir(entry_path):
            subfolders, sub_total_pages = scan_folder(base_dir, os.path.join(rel_path, entry))
            folder_data.extend(subfolders)
            total_pages_folder += sub_total_pages

    # Add current folder info if it has any PDFs
    if folder_pdf_files:
        folder_data.insert(0, {
            "name": rel_path,
            "pdf_files": folder_pdf_files,
            "total_pages": sum(f["pages"] for f in folder_pdf_files)
        })

    return folder_data, total_pages_folder

if __name__ == "__main__":
    base_dir = "/Users/nuraratsangreuang/Documents/PEA_ProInside"  # Change this
    folders, total_pages_all = scan_folder(base_dir)
    result = {
        "folders": folders,
        "total_pages_all_folders": total_pages_all
    }
    print(json.dumps(result, indent=2))