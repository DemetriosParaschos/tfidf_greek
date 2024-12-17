### File path: main.py

""" main.py

This script analyses a corpus of text files to perform text cleaning, corpus creation, TF-IDF calculation, word sorting, and result visualisation.

Functions:
- main: The main function that handles the workflow of text analysis.

Modules:
- utils: Contains helper functions including:
  - get_all_txt_file_paths: Retrieves all .txt file paths from a directory.
  - text_cleaning_lemmas: Cleans and processes text files into lemmas.
  - creating_corpus: Creates a corpus of texts and counts total .txt files.
  - word_search: Performs word searching in a given corpus.
  - calculate_idf: Calculates the IDF (Inverse Document Frequency) of words.
  - generate_visualisations: Generates visualisations for word analysis results.
  - save_results_to_folder: Saves analysis results to specified folders.

Usage:
Run as a standalone script to process Greek texts for analysis.
"""

# Import required functions from utils.py
from utils import (get_all_txt_file_paths,
                   text_cleaning_lemmas,
                   creating_corpus,
                   word_search,
                   calculate_idf,
                   generate_visualisations,
                   save_results_to_folder)


def main(corpus_path, analysis_path, visualisations=True, save_results=False):
    """ Main function for text analysis pipeline.

    Parameters:
    - corpus_path (str): Path to the folder containing corpus text files.
    - analysis_path (str): Path to the folder containing analysis text files.
    - visualisations (bool): Whether to generate visualisations. Default is True.
    - save_results (bool): Whether to save the analysis results. Default is False.

    Workflow:
    1. Retrieves text file paths for corpus and analysis.
    2. Cleans and processes the analysis files into lemmas.
    3. Creates a text corpus and counts the total number of text files.
    4. Performs word searches within the corpus.
    5. Calculates the IDF of words in the analysis.
    6. Sorts words based on TF-IDF scores.
    7. Prints the top 50 words with the highest TF-IDF scores.
    8. Optionally generates visualisations and saves results.
    """
    # Step 1: Retrieve file paths
    corpus_files = get_all_txt_file_paths(corpus_path)  # List of corpus text files
    analysis_files = get_all_txt_file_paths(analysis_path)  # List of analysis files

    # Step 2: Clean and process analysis files
    x = text_cleaning_lemmas(analysis_files)

    # Step 3: Create corpus and count text files
    corpus_texts, total_number_of_txt_files = creating_corpus(corpus_path)

    # Step 4: Perform word search within corpus
    word_search(corpus_texts, x)

    # Step 5: Calculate IDF for words
    calculate_idf(total_number_of_txt_files, x)

    # Step 6: Sort words by TF-IDF score
    sorted_words = sorted(x, key=lambda word_obj: word_obj.tf_idf, reverse=True)

    # Step 7: Print top 50 words for reference
    for word in sorted_words[:50]:
        print(f'Word: {word.word}, score: {word.tf_idf}')

    # Step 8: Generate visualisations if requested
    if visualisations:
        generate_visualisations(sorted_words)

    # Step 9: Save results if requested
    if save_results:
        save_results_to_folder(x, sorted_words, corpus_path, corpus_files, analysis_path, analysis_files,
                               save_results=True)


if __name__ == "__main__":
    """ Execution starts here.

    The script runs the main function with preset paths for:
    - corpus_path: Path to corpus texts.
    - analysis_path: Path to group analysis files.

    Visualisations and result saving are enabled.
    """
    corpus_path = "greek_texts/texts"  # Path to corpus directory
    analysis_path = "greek_texts/groups/stoic"  # Path to analysis group directory
    main(corpus_path, analysis_path, visualisations=True, save_results=True)
