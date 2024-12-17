# TF-IDF Analysis of Greek Texts: Vocabulary Comparison in Poetry

## Overview
This project explores **thematic vocabulary differences** in Greek poetry, particularly focusing on **hymns dedicated to Zeus**. The aim is to compare vocabulary usage across poems of various eras (Archaic to Hellenistic) and philosophical orientation (Classical, Orphic, Stoic, Alexandrian, Neoplatonic, etc.) to identify distinct word patterns and their significance.

The approach leverages **TF-IDF** (Term Frequency-Inverse Document Frequency) analysis to highlight words that are important in a specific subcorpus but uncommon across the entire corpus. The results contribute to broader projects, such as **VERITRACE** (focused on Orphic poems) and ongoing research into Stoic poetry.

---

## Project Goals
1. **Vocabulary Analysis**: Identify words with high TF-IDF scores in the entire corpus and compare them to subgroups.
2. **Thematic Exploration**: Study how different poetic traditions address the figure of Zeus.
3. **Digital Humanities Application**: Apply **Natural Language Processing (NLP)** tools for Ancient Greek.
4. **Critical Editions**: Utilise texts from established critical editions.
5. **Publication**: Analyse and prepare findings for academic publication.
6. **Corpus Flexibility**: Expand the corpus beyond poetry to other types of Greek texts as needed.

---

## Corpus
### Text Selection
The texts include hymns dedicated to Zeus, sourced from critical editions and organised into subcorpora. The corpus is flexible and can be expanded to include non-poetic texts as well.

### Hymns to Zeus
- **Homeric Hymn 23**: To Zeus 
- **Callimachus, Hymn 1**: To Zeus
- **Orphic Hymn 15**: To Zeus
- **Orphic Hymn 19**: To Zeus the Thunderbolt
- **Orphic Hymn 20**: To Astrapaios Zeus
- **Derveni Papyrus, Col. XV-XIX**
- **Aratus, *Phaenomena***: Lines 1-18

---

## VERITRACE Context
This project operates within the broader scope of the **VERITRACE** project, which focuses on the collection, analysis, and digital preservation of **Orphic texts**. VERITRACE applies digital humanities methodologies to reconstruct Orphic traditions and analyse their impact on later literature and philosophy. The current subproject aligns with VERITRACE's goals by:

- Exploring the Orphic vocabulary and its distinct usage.
- Comparing Orphic themes with other poetic and philosophical traditions, such as Stoic texts.
- Highlighting how digital tools like **TF-IDF** enhance textual analysis.

For more information on VERITRACE, please visit our [website](https://veritrace.eu).

---

## Project Structure
The project is modular, with functionality divided into multiple Python scripts located in the `utils` folder:

```
.
├── main.py                   # Main script to run the analysis
├── utils/                    # Modular utilities for processing
│   ├── classes.py           # Word class and data structures
│   ├── corpus_processing.py # Corpus and file handling utilities
│   ├── file_operations.py   # File I/O management
│   ├── save_results.py      # Save metadata and results
│   ├── text_processing.py   # Text normalisation and lemmatisation
│   ├── tfidf_analysis.py    # TF-IDF calculation and analysis
│   └── visualisations.py    # Visualisations (Bar Chart, Word Cloud)
├── greek_texts/             # Corpus and grouped subcorpora
│   ├── texts/               # Main corpus
│   └── groups/              # Subcorpora
├── static/fonts/            # Fonts for WordCloud visualisations
└── results/                 # Output results (generated dynamically)
```

---

## Features
### 1. Text Preprocessing
- **Normalisation**: Text cleaning for Ancient Greek, including punctuation handling and accent normalisation (grave to acute).
- **Lemmatisation**: Using **CLTK's GreekBackoffLemmatizer** for morphological analysis.

### 2. TF-IDF Analysis
- Calculates **Term Frequency-Inverse Document Frequency** for words.
- Identifies words significant to a subcorpus but uncommon in the entire corpus.

### 3. Visualisation
- **Bar Charts**: Top words by raw frequency and TF-IDF score.
- **Word Clouds**: Visual representation of TF-IDF scores.

### 4. Metadata and Results
- Results are saved dynamically with a timestamp.
- **YAML Metadata** includes system information, file paths, and word count statistics.
- **Excel Output**: Full analysis of words, including:
  - Raw Count
  - Frequency (%)
  - IDF Score
  - TF-IDF Score
  - Found in Texts (Number of appearances in subcorpora)

---

## Installation
### Requirements
Install the necessary Python libraries:

```bash
pip install -r requirements.txt
```

### Dependencies
- **Python 3.9**

- **CLTK** (Classical Language Toolkit)
- **Matplotlib**
- **WordCloud**
- **Pandas**
- **PyYAML**
- **tqdm**

---

## Usage
### Run the Analysis
Run the main script with the following paths:

```bash
python main.py
```

Modify paths as needed:
```python
corpus_path = '/path/to/greek_texts/texts/'
analysis_path = '/path/to/greek_texts/groups/stoic'
```

### Output
- Results are saved in the `results/` folder with dynamically named subfolders.
- **Excel File**: Word analysis.
- **Visualisations**: Bar chart and WordCloud images.
- **YAML Metadata**: Detailed information about the analysis.

---

## Critical Editions
The following critical editions were consulted for the texts:
1. T.W. Allen, W.R. Halliday, and E.E. Sikes, _The Homeric hymns_, 2nd edn., Oxford: Clarendon Press, 1936. 
2. R. Pfeiffer, _Callimachus_, vol. 2, Oxford: Clarendon Press, 1953.
3. W. Quandt, _Orphei hymni_, 3rd edn., Berlin: Weidmann, 1962 (repr. 1973).
4. \[Anon.], "Der orphische Papyrus von Derveni," _Zeitschrift für Papyrologie und Epigraphik_ 47 (1982). 
5. J.-M. Martin, _Arati phaenomena_, Florence: La Nuova Italia Editrice, 1956.

---

## Challenges and Future Work
1. **NLP Limitations**: The accuracy of lemmatisation and TF-IDF for Ancient Greek remains challenging.
2. **Phrases and Metre**: How does the analysis adapt to poetic metre and phrasing?
3. **Cross-Linguistic Comparison**: Results may differ significantly in Latin translations.
4. **Corpus Expansion**: Including texts from the Byzantine era (e.g., Gemistos Plethon) could add another dimension.
5. **Publishing Results**: Preparing outputs for publication as a paper and GitHub repository.

---

## Acknowledgements
This project connects to the **[VERITRACE](https://veritrace.eu)** project and my ongoing PhD research focused on Stoic texts.

---

## License
This project is licensed under the MIT License.

