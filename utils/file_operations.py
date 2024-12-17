# File path: utils/file_operations.py

""" file_operations.py

This module provides functions for reading text files and retrieving all `.txt` file paths
from a given folder or directory structure.

Functions:
- get_data: Reads the content of a single text file and returns it as a string.
- get_all_txt_file_paths: Retrieves all `.txt` file paths in a directory, including subdirectories.

Usage:
These functions are used to load data for text processing workflows.
"""

import os


def get_data(filename: str) -> str:
    """Reads text from a file.

    Parameters:
    - filename (str): The path to the file to be read.

    Returns:
    - str: The content of the file as a string.

    Example:
    >>> content = get_data("example.txt")
    >>> print(content)
    """
    with open(filename, "r") as f:
        return f.read()


def get_all_txt_file_paths(main_folder):
    """Retrieves all `.txt` file paths from a folder, including subdirectories.

    Parameters:
    - main_folder (str): The path to the main folder or `.txt` file.

    Returns:
    - list: A list of file paths pointing to `.txt` files.

    Workflow:
    - If `main_folder` is a single `.txt` file, it adds that to the list.
    - Otherwise, it recursively searches for `.txt` files in the folder and subfolders.

    Example:
    >>> txt_files = get_all_txt_file_paths("my_folder")
    >>> print(txt_files)

    Notes:
    - Uses os.walk to traverse the directory structure.
    - Filters files with `.txt` extension.
    """
    txt_file_paths = []

    # If the provided path itself is a `.txt` file
    if main_folder.endswith('.txt'):
        txt_file_paths.append(main_folder)
    else:
        # Walk through the directory structure
        for root, _, files in os.walk(main_folder):
            for file in files:
                if file.endswith('.txt'):
                    # Construct the full path and add to the list
                    txt_file_paths.append(os.path.join(root, file))

    return txt_file_paths
