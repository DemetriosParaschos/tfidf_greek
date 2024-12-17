# File path: utils/corpus_processing.py

""" corpus_processing.py

This module provides functions for processing and creating text corpora.
It leverages text cleaning, normalisation, and lemmatisation utilities
for structured text analysis.

Functions:
- process_corpus: Cleans and processes all text files in a given corpus path.
- creating_corpus: Generates a corpus from text files and counts the total number of files.

Dependencies:
- utils: Contains helper functions such as get_all_txt_file_paths and text_cleaning_lemmas.
- tqdm: Used to display progress bars for file processing tasks.

Usage:
These functions are essential for preparing text data for further
analysis, such as TF-IDF calculations or word frequency visualisations.
"""

from utils import get_all_txt_file_paths, text_cleaning_lemmas
from tqdm import tqdm


def process_corpus(corpus_path, normalize_proc, lemmatizer):
    """Processes the entire corpus and returns cleaned, lemmatised texts.

    Parameters:
    - corpus_path (str): Path to the folder containing corpus text files.
    - normalize_proc (function): Function for normalising text data.
    - lemmatizer (object): Lemmatizer to transform words into their base form.

    Returns:
    - list: A list of cleaned and lemmatised texts.

    Workflow:
    1. Retrieves all text file paths from the specified folder.
    2. Cleans and processes each text file into lemmatised tokens.
    3. Joins tokens into a single string per file.

    Example:
    >>> processed_texts = process_corpus("data/corpus", normalize_func, lemmatizer)
    >>> print(processed_texts[0])
    """
    txt_files = get_all_txt_file_paths(corpus_path)  # Retrieve .txt files
    corpus_texts = []

    print("Processing corpus files...")
    for file_path in tqdm(txt_files, desc="Files"):
        # Clean and lemmatise text content
        cleaned_text = text_cleaning_lemmas([file_path], normalize_proc, lemmatizer)
        corpus_texts.append(" ".join(cleaned_text))  # Combine tokens into a single string

    return corpus_texts


def creating_corpus(folder_path):
    """Creates a text corpus from files and counts the total number of text files.

    Parameters:
    - folder_path (str): Path to the folder containing text files.

    Returns:
    - tuple: (list of corpus texts, total number of text files)

    Workflow:
    1. Retrieves all `.txt` files from the specified folder.
    2. Processes each file using `text_cleaning_lemmas`.
    3. Counts the total number of files processed.

    Example:
    >>> corpus, total_files = creating_corpus("data/texts")
    >>> print(f"Total files: {total_files}")

    Notes:
    - Uses tqdm to display progress as files are processed.
    - Each processed text remains tokenised (not joined into strings).
    """
    txt_files = get_all_txt_file_paths(folder_path)  # Retrieve all text file paths
    total_number_of_txt_files = len(txt_files)  # Count total files
    corpus_texts = []

    # Use tqdm to show file processing progress
    for file_path in tqdm(txt_files, desc="Processing files", unit="file"):
        # Clean and process text content
        text = text_cleaning_lemmas([file_path], analysis=False)
        corpus_texts.append(text)

    return corpus_texts, total_number_of_txt_files
