# File path: utils/save_results.py

""" save_results.py

This module handles saving analysis results, metadata, and visualisations to a specified results folder.
It supports exporting data as YAML and Excel files and generates bar charts and word clouds
for text analysis outcomes.

Functions:
- save_results_to_folder: Saves word analysis results, metadata, and visualisations to a folder.

Dependencies:
- sys: For retrieving Python version information.
- yaml: For exporting metadata to a YAML file.
- platform: For accessing operating system details.
- pandas: For exporting word data to Excel.
- pathlib: For creating folder paths.
- matplotlib.pyplot: For generating bar chart visualisations.
- wordcloud: For creating word cloud visualisations.
- datetime: For timestamp generation to name result folders.

Usage:
Call `save_results_to_folder` with appropriate word analysis results to save outputs.
"""

import sys
import yaml
import platform
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from datetime import datetime


def save_results_to_folder(words_list, sorted_words, corpus_path, corpus_files, analysis_path, analysis_files,
                           save_results=False):
    """Saves analysis results, metadata, and visualisations to a timestamped folder.

    Parameters:
    - words_list (list): A list of Word objects containing word statistics.
    - sorted_words (list): Words sorted by TF-IDF scores.
    - corpus_path (str): Path to the corpus directory.
    - corpus_files (list): List of corpus file paths.
    - analysis_path (str): Path to the analysis directory.
    - analysis_files (list): List of analysis file paths.
    - save_results (bool): Flag to enable saving results. Default is False.

    Workflow:
    1. Creates a timestamped results folder.
    2. Saves metadata about the analysis process in a YAML file.
    3. Exports word statistics as an Excel file.
    4. Generates a bar chart visualising the top 20 words by raw occurrences.
    5. Creates a word cloud based on TF-IDF scores.

    Example:
    >>> save_results_to_folder(words_list, sorted_words, "data/corpus", corpus_files,
                              "data/analysis", analysis_files, save_results=True)

    Notes:
    - Visualisations are saved as PNG files in the results folder.
    - Metadata includes system information, file paths, and word analysis summaries.
    """
    if not save_results:
        return

    # Generate folder name with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_folder = Path(f'results/results_{timestamp}')
    results_folder.mkdir(parents=True, exist_ok=True)

    # Save metadata as YAML
    metadata_file = results_folder / "metadata.yaml"
    metadata = {
        "spec": "1.0",
        "metadata": {
            "generated_on": str(datetime.now()),
            "system_info": {
                "os": platform.system() + " " + platform.release(),
                "python_version": sys.version.split()[0]
            },
            "word_counts": {
                "total_words_analyzed": len(words_list),
                "total_unique_words": len(set([w.word for w in words_list]))
            }
        },
        "data": {
            "corpus": {
                "path": corpus_path,
                "file_count": len(corpus_files),
                "files": corpus_files
            },
            "analysis": {
                "path": analysis_path,
                "file_count": len(analysis_files),
                "files": analysis_files
            }
        }
    }
    with open(metadata_file, "w") as f:
        yaml.dump(metadata, f, default_flow_style=False, allow_unicode=True)

    # Save data to Excel
    excel_file = results_folder / "results.xlsx"
    data = {
        'Word': [w.word for w in words_list],
        'Raw Count': [w.raw_count for w in words_list],
        'Frequency (%)': [w.frequency for w in words_list],
        'IDF': [w.idf for w in words_list],
        'TF-IDF': [w.tf_idf for w in words_list],
        'Found in Texts': [w.found_in_texts for w in words_list]
    }
    df = pd.DataFrame(data)
    df.sort_values(by='TF-IDF', ascending=False, inplace=True)
    df.to_excel(excel_file, index=False)

    # Save visualisations
    top_words = sorted_words[:20]  # Top 20 words
    words = [w.word for w in top_words]
    raw_counts = [w.raw_count for w in top_words]

    # Save bar chart
    bar_chart_file = results_folder / "bar_chart.png"
    plt.figure(figsize=(10, 6))
    plt.barh(words[::-1], raw_counts[::-1], color='skyblue')
    plt.xlabel('Occurrences in the text')
    plt.title(f'Top 20 Words by TF-IDF Score\n(X-axis shows raw occurrences)')
    plt.tight_layout()
    plt.savefig(bar_chart_file)
    plt.close()

    # Save word cloud
    word_freq = {w.word: w.tf_idf for w in sorted_words if w.tf_idf > 0}
    wordcloud_file = results_folder / "word_cloud.png"
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
    plt.savefig(wordcloud_file)
    plt.close()

    print(f"Results saved in folder: {results_folder}")
