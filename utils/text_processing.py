# File path: utils/text_processing.py

""" text_processing.py

This module provides functions for cleaning, normalising, and lemmatising Ancient Greek text.
It uses the Classical Language Toolkit (CLTK) for lemmatisation and text processing.

Functions:
- get_greek_lemmatizer: Retrieves a Greek lemmatiser, ensuring the required CLTK corpus is downloaded.
- cleaning_greek_text: Cleans and normalises Ancient Greek text.
- replace_grave_with_acute: Replaces grave-accented vowels with acute-accented counterparts.
- lemmatizing_text_cltk: Tokenises, normalises, and lemmatises text using the CLTK library.
- text_cleaning_lemmas: Combines text cleaning, lemmatisation, and optional statistical analysis for text files.

Dependencies:
- CLTK: Used for normalisation and lemmatisation.
- re: For regular expressions to clean and process text.
- string: Provides punctuation handling utilities.
- utils: Imports helper functions for statistical analysis and file operations.

Usage:
These functions are utilised to prepare Ancient Greek texts for word analysis and further processing.
"""

import re
import string
from cltk.core.data_types import Doc
from cltk.data.fetch import FetchCorpus
from cltk.lemmatize.grc import GreekBackoffLemmatizer
from cltk.alphabet.processes import GreekNormalizeProcess
from cltk.alphabet.text_normalization import split_leading_punct, split_trailing_punct, remove_odd_punct

from .text_processing import *
from .tfidf_analysis import statistical_analysing, words_to_objects
from .file_operations import get_data


def get_greek_lemmatizer():
    """Retrieves a Greek lemmatiser from CLTK. Downloads corpus if not found.

    Returns:
    - GreekBackoffLemmatizer: An instance of the lemmatiser.
    """
    try:
        lemmatizer_download = GreekBackoffLemmatizer()
    except FileNotFoundError as e:
        if 'grc_models_cltk' in str(e):
            corpus_downloader = FetchCorpus(language="grc")
            corpus_downloader.import_corpus("grc_models_cltk")
            lemmatizer_download = GreekBackoffLemmatizer()
        else:
            raise e
    return lemmatizer_download


lemmatizer = get_greek_lemmatizer()
lang = "grc"
normalize_proc = GreekNormalizeProcess(language=lang)


def cleaning_greek_text(text) -> str:
    """Cleans and normalises Ancient Greek text.

    Parameters:
    - text (str): The raw Ancient Greek text.

    Returns:
    - str: Cleaned and normalised text.
    """
    # Normalize the text for Ancient Greek
    non_normed_doc = Doc(raw=text)
    normalized_doc = normalize_proc.run(input_doc=non_normed_doc)
    normalized_text = normalized_doc.raw

    # Remove odd punctuation and ensure correct punctuation splitting
    normalized_text = remove_odd_punct(normalized_text)
    normalized_text = split_trailing_punct(normalized_text)
    normalized_text = split_leading_punct(normalized_text)

    # Replace certain quotation marks
    normalized_text = normalized_text.replace('«', "'").replace('»', "'")

    # Clean whitespace
    normalized_text = re.sub(r'\ +', ' ', normalized_text)
    normalized_text = re.sub(r'\n+', '\n', normalized_text)
    normalized_text = re.sub(r'^\s+', '', normalized_text, flags=re.MULTILINE)

    return normalized_text


# Define the mapping from grave-accented to acute-accented vowels
grave_to_acute_map = {
    'ὰ': 'ά',
    'ὲ': 'έ',
    'ὴ': 'ή',
    'ὶ': 'ί',
    'ὺ': 'ύ',
    'ὸ': 'ό',
    'ὼ': 'ώ'
}


def replace_grave_with_acute(word: str) -> str:
    """Replaces grave-accented vowels in a word with their acute counterparts.

    Parameters:
    - word (str): The input word containing grave-accented vowels.

    Returns:
    - str: Word with grave accents replaced by acute accents.
    """
    for grave, acute in grave_to_acute_map.items():
        word = word.replace(grave, acute)
    return word


def lemmatizing_text_cltk(text: str) -> str:
    """Tokenises, normalises, and lemmatises Ancient Greek text.

    Parameters:
    - text (str): The raw input text.

    Returns:
    - str: A lemmatised and cleaned version of the text.
    """
    custom_punctuation = string.punctuation + "·«»⟦⟧…"

    # Initial punctuation handling
    text = split_trailing_punct(text, punctuation=list(custom_punctuation))
    text = split_leading_punct(text, punctuation=list(custom_punctuation))
    text = remove_odd_punct(text)

    # Normalize the text for Ancient Greek
    non_normed_doc = Doc(raw=text)
    normalized_doc = normalize_proc.run(input_doc=non_normed_doc)
    normalized_text = normalized_doc.raw

    # Remove editorial markers
    normalized_text = re.sub(r'col\d+', '', normalized_text)
    normalized_text = re.sub(r'±\d+', '', normalized_text)
    normalized_text = re.sub(r'\[.*?\]', '', normalized_text)
    normalized_text = re.sub(r'[⏑–†]', '', normalized_text)

    # Tokenise and clean tokens
    tokenized_text = normalized_text.split()
    tokens_cleaned = []
    for t in tokenized_text:
        t = re.sub(rf'^[{re.escape(custom_punctuation)}]+|[{re.escape(custom_punctuation)}]+$', '', t)
        t = replace_grave_with_acute(t)
        if t:
            tokens_cleaned.append(t)

    # Lemmatise cleaned tokens
    text_lemmas = lemmatizer.lemmatize(tokens_cleaned)
    lemmas = [tup[1].lower() for tup in text_lemmas]

    # Post-process tokens
    cleaned = []
    for lemma in lemmas:
        if lemma in ['punc', 'col']:
            continue
        if lemma == 'δ':
            lemma = 'δέ'
        cleaned.append(lemma)

    return ' '.join(cleaned)


def text_cleaning_lemmas(file_path, analysis=True):
    """Combines text cleaning, lemmatisation, and optional statistical analysis.

    Parameters:
    - file_path (list): List of file paths containing Ancient Greek text.
    - analysis (bool): Whether to perform statistical analysis. Default is True.

    Returns:
    - list or str: Word objects with analysis results if `analysis` is True, otherwise lemmatised text.
    """
    main_text = ''
    for path in file_path:
        if main_text:
            main_text += '\n'
        main_text += get_data(path)
    cleaned_text = cleaning_greek_text(main_text)
    lemmatized_text = lemmatizing_text_cltk(cleaned_text)
    if analysis:
        analysed_text = statistical_analysing(lemmatized_text)
        word_list = words_to_objects(analysed_text)
        return word_list
    else:
        return lemmatized_text
