import zipfile
import os
import json
import logging
from typing import List, Dict

def unzip_data(source: str, destination: str):
    with zipfile.ZipFile(source, "r") as zip_ref:
        zip_ref.extractall(destination)

def load_data_from_file(file_path: str) -> List[Dict]:
    """Load JSON data from a file."""
    logging.info(f"Loading data from {file_path}")
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def initialize_data(data_directory: str) -> List[Dict]:
    """Initialize and return data from the extracted files."""
    data = []
    for filename in os.listdir(data_directory):
        file_path = os.path.join(data_directory, filename)
        data.extend(load_data_from_file(file_path))
    return data