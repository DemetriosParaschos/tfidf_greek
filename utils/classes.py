# File path: utils/classes.py

""" classes.py

This module defines the `Word` class used for text analysis purposes.

Class:
- Word: Represents a word with attributes for frequency, raw count, IDF, TF-IDF score, and the number of texts it appears in.

Attributes:
- word (str): The word itself.
- frequency (float): The frequency of the word (default is 0).
- raw_count (int): The raw count of occurrences in the text (default is 0).
- idf (float): The Inverse Document Frequency score of the word (default is 0).
- tf_idf (float): The Term Frequency-Inverse Document Frequency score of the word (default is 0).
- found_in_texts (int): The number of texts in which the word was found (default is 0).

Usage:
This class is utilised to store word statistics during the TF-IDF calculation process.
"""

class Word:
    def __init__(self, word, frequency=0, raw_count=0, idf=0, tf_idf=0):
        """Initialises a Word object with specified attributes.

        Parameters:
        - word (str): The word itself.
        - frequency (float, optional): Word frequency. Defaults to 0.
        - raw_count (int, optional): Raw count of word occurrences. Defaults to 0.
        - idf (float, optional): IDF score of the word. Defaults to 0.
        - tf_idf (float, optional): TF-IDF score of the word. Defaults to 0.
        """
        self.word = word  # The word string
        self.frequency = frequency  # Frequency of the word
        self.raw_count = raw_count  # Raw occurrence count in text
        self.idf = idf  # Inverse Document Frequency score
        self.tf_idf = tf_idf  # TF-IDF score
        self.found_in_texts = 0  # Number of texts where the word was found
