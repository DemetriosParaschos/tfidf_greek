# File path: utils/visualisation.py

""" visualisation.py

This module generates visualisations for word analysis results, including bar charts
and word clouds, based on TF-IDF scores.

Functions:
- generate_visualisations: Creates bar charts and word clouds for the top words
  based on TF-IDF analysis.

Dependencies:
- matplotlib.pyplot: For creating bar chart visualisations.
- wordcloud: For generating word clouds.
- datetime: For generating timestamps to save visualisations.

Usage:
Call `generate_visualisations` with a list of sorted words to generate visual outputs.
"""

import matplotlib.pyplot as plt
from wordcloud import WordCloud
from datetime import datetime


def generate_visualisations(sorted_words, top_n=20, save_figures=False):
    """Generates bar charts and word clouds for word analysis results.

    Parameters:
    - sorted_words (list): A list of Word objects sorted by TF-IDF scores.
    - top_n (int, optional): Number of top words to include in the bar chart. Default is 20.
    - save_figures (bool, optional): If True, saves the figures as PNG files. Default is False.

    Workflow:
    1. Generates a bar chart for the top N words sorted by TF-IDF scores.
    2. Creates a word cloud based on TF-IDF scores of the words.
    3. Optionally saves visualisations with a timestamp.

    Outputs:
    - Displays the bar chart and word cloud.
    - Saves the figures if `save_figures` is set to True.

    Example:
    >>> generate_visualisations(sorted_words, top_n=10, save_figures=True)
    """
    # Generate a timestamp for file naming
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Visualisation 1: Bar Chart of Top TF-IDF Words
    top_words = sorted_words[:top_n]
    words = [w.word for w in top_words]
    raw_counts = [w.raw_count for w in top_words]

    plt.figure(figsize=(10, 6))
    plt.barh(words[::-1], raw_counts[::-1], color='skyblue')
    plt.xlabel('Occurrences in the text')
    plt.title(f'Top {top_n} Words by TF-IDF Score\n(X-axis shows raw occurrences)')
    plt.tight_layout()

    if save_figures:
        plt.savefig(f'top_tf_idf_words_{timestamp}.png')
        plt.close()
    else:
        plt.show()

    # Visualisation 2: Word Cloud Based on TF-IDF Scores
    word_freq = {w.word: w.tf_idf for w in sorted_words if w.tf_idf > 0}
    wc = WordCloud(
        width=800,
        height=400,
        background_color='white',
        colormap='Dark2',
        font_path='static/fonts/EBGaramond-VariableFont_wght.ttf'
    )
    wc.generate_from_frequencies(word_freq)

    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud Based on TF-IDF Scores')

    if save_figures:
        plt.savefig(f'word_cloud_{timestamp}.png')
        plt.close()
    else:
        plt.show()
