### File path: utils/__init__.py

""" __init__.py

This script initialises the utils package by importing various modules required for text analysis.

Modules:
- classes: Contains definitions for text-related classes, including Word objects.
- file_operations: Handles file retrieval and operations such as reading and writing text files.
- visualisations: Contains functions for generating visual representations of word analysis results.
- text_processing: Provides tools for text cleaning, tokenisation, and lemmatisation.
- tfidf_analysis: Calculates and analyses TF-IDF scores for words in a text corpus.
- save_results: Manages saving analysis results into files or folders.
- corpus_processing: Facilitates corpus creation and word searching.

Usage:
By importing this package, all core functionalities are made available for text analysis workflows.
"""

# Import required modules from utils package
from .classes import *            # Import text-related class definitions
from .file_operations import *    # Import file retrieval and operation functions
from .visualisations import *     # Import visualisation tools
from .text_processing import *    # Import text cleaning and processing functions
from .tfidf_analysis import *     # Import TF-IDF calculation tools
from .save_results import *       # Import result saving utilities
from .corpus_processing import *  # Import corpus creation and word search functions
