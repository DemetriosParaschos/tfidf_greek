# File path: utils/tfidf_analysis.py

""" tfidf_analysis.py

This module provides functions for analysing text frequency, calculating IDF and TF-IDF scores,
and performing word searches in a text corpus.

Functions:
- statistical_analysing: Performs word frequency analysis.
- words_to_objects: Converts word frequency data into Word objects.
- calculate_idf: Calculates IDF (Inverse Document Frequency) and TF-IDF scores for words.
- word_search: Searches for words within a corpus and updates their appearance count.

Dependencies:
- math: For logarithmic calculations in IDF.
- collections.Counter: To calculate word frequencies.
- utils.classes.Word: Word class definition for storing word attributes.

Usage:
These functions form the backbone of TF-IDF analysis pipelines for Ancient Greek text processing.
"""

import math
from collections import Counter
from .classes import Word


def statistical_analysing(text: str) -> dict:
    """Performs word frequency analysis on a given text.

    Parameters:
    - text (str): Input text for word analysis.

    Returns:
    - dict: A dictionary containing:
        - 'Word': List of unique words in the text.
        - 'Raw Count': Number of occurrences of each word.
        - 'Frequency (%)': Frequency of each word as a percentage of total words.

    Example:
    >>> text = "apple orange apple"
    >>> stats = statistical_analysing(text)
    >>> print(stats)
    {'Word': ['apple', 'orange'], 'Raw Count': [2, 1], 'Frequency (%)': [0.6667, 0.3333]}
    """
    words_list = text.lower().split()
    total_words = len(words_list)
    word_counts = Counter(words_list)
    return {
        'Word': list(word_counts.keys()),
        'Raw Count': list(word_counts.values()),
        'Frequency (%)': [count / total_words for count in word_counts.values()]
    }


def words_to_objects(words_data: dict) -> list:
    """Converts word frequency data into a list of Word objects.

    Parameters:
    - words_data (dict): A dictionary containing word statistics:
        - 'Word': List of words.
        - 'Frequency (%)': List of word frequencies.
        - 'Raw Count': List of word occurrence counts.

    Returns:
    - list: A list of Word objects.

    Example:
    >>> data = {'Word': ['apple'], 'Frequency (%)': [0.5], 'Raw Count': [1]}
    >>> word_objects = words_to_objects(data)
    >>> print(word_objects[0].word, word_objects[0].frequency)
    apple 0.5
    """
    word_objects_list = [Word(word, frequency, raw_count) for word, frequency, raw_count in
                         zip(words_data['Word'], words_data['Frequency (%)'], words_data['Raw Count'])]
    return word_objects_list


def calculate_idf(number_of_documents: int, word_objects: list) -> None:
    """Calculates IDF and TF-IDF scores for each word object.

    Parameters:
    - number_of_documents (int): Total number of documents in the corpus.
    - word_objects (list): List of Word objects.

    Workflow:
    - If a word is not found in any document, it is assigned a high TF-IDF value (default 10000).
    - Otherwise, the IDF is calculated as log(number_of_documents / found_in_texts).
    - TF-IDF is then calculated as IDF multiplied by raw count.

    Example:
    >>> word_obj = Word('apple', raw_count=3, found_in_texts=2)
    >>> calculate_idf(10, [word_obj])
    >>> print(word_obj.idf, word_obj.tf_idf)
    """
    for word_obj in word_objects:
        if word_obj.found_in_texts == 0:
            word_obj.tf_idf = 10000  # Assign a high TF-IDF value for unique words
        else:
            word_obj.idf = math.log((number_of_documents / word_obj.found_in_texts))
            word_obj.tf_idf = word_obj.idf * word_obj.raw_count


def word_search(corpus: list, words_objects: list) -> None:
    """Searches for words within a corpus and updates their appearance count.

    Parameters:
    - corpus (list): A list of text strings representing the corpus.
    - words_objects (list): A list of Word objects to search for in the corpus.

    Workflow:
    - Creates a set of words to be searched for quick lookup.
    - Iterates through each text in the corpus and finds matching words.
    - Updates the 'found_in_texts' attribute for matching Word objects.

    Example:
    >>> corpus = ["apple orange", "banana apple"]
    >>> word_objs = [Word("apple"), Word("orange")]
    >>> word_search(corpus, word_objs)
    >>> print(word_objs[0].found_in_texts)
    2
    """
    words_set = {word_obj.word for word_obj in words_objects}  # Create a set of target words
    for text in corpus:  # Iterate through texts in corpus
        text_words = set(text.split())  # Convert text to a set of words
        found_words = text_words.intersection(words_set)  # Find words in both sets
        for word in found_words:  # Increment count for matched words
            for word_obj in words_objects:
                if word == word_obj.word:
                    word_obj.found_in_texts += 1
