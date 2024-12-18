# TF-IDF Analysis of Greek Texts: Vocabulary Comparison in Poetry

## Overview
This project explores **thematic vocabulary differences** in Greek poetry, particularly focusing on **hymns dedicated to Zeus**. The aim is to compare vocabulary usage across poems of various eras (Archaic to Hellenistic) and philosophical orientations (Classical, Orphic, Stoic, Alexandrian, Neoplatonic, etc.) to identify distinct word patterns and their significance.

The approach leverages **TF-IDF** ([Term Frequency-Inverse Document Frequency](https://en.wikipedia.org/wiki/Tf–idf)) analysis to highlight words that are important in a specific subcorpus but uncommon across the entire corpus. The results contribute to broader projects, such as **VERITRACE** (focused on Orphic poems) and ongoing research into Stoic poetry.

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
- **Aratus, *Phaenomena***: Lines 1-18
- **Callimachus, Hymn 1**: To Zeus
- **Cleanthes, Fragment 1**: Hymn to Zeus
- **Derveni Papyrus**: Col. XV-XIX
- **Homeric Hymn 23**: To Zeus 
- **Orphic Hymn 15**: To Zeus
- **Orphic Hymn 19**: To Zeus the Thunderbolt
- **Orphic Hymn 20**: To Astrapaios Zeus

---

## VERITRACE Context  
This mini-project operates within the scope of the **VERITRACE** project, an ERC-funded initiative led by **Prof. Dr. Cornelis J. Schilt**, research professor at the **Vrije Universiteit Brussel**. VERITRACE, also known as *Traces de la Verité*, addresses the influence of ancient wisdom writings on the development of early modern natural philosophy.  

During the Renaissance, works such as the **Chaldean Oracles**, the **Sibylline Oracles**, the **Corpus Hermeticum**, and the **Orphic Hymns** were rediscovered and incorporated into a *prisca sapientia*—a tradition that viewed these texts as containing timeless truths about God, humanity, and the cosmos. Foundational figures of modern science, including **Nicolaus Copernicus**, **Johannes Kepler**, **Francis Bacon**, **Pierre Gassendi**, **Isaac Newton**, and **Gottfried Wilhelm Leibniz**, engaged with this tradition, yet no comprehensive account has existed of precisely what they adopted from these texts or how the notion of a perennial truth shaped their knowledge-making.  

VERITRACE explores these questions by deploying **bespoke distant reading techniques** on a vast corpus of early modern printed works. It traces the reappearance and dissemination of prominent ancient wisdom writings within early modern natural philosophy, examining:  

- **What** early modern thinkers adopted from these texts.  
- **How** these writings functioned within the emerging scientific discourse.  
- **The debates** surrounding these ancient wisdom texts across early modern Europe, capturing the diversity of perceptions and interpretations.  

By doing so, VERITRACE addresses a major gap in understanding the role of *prisca sapientia* in the emergence and evolution of early modern science.  

### Alignment of the Current Mini-Project  
The current mini-project contributes to VERITRACE’s overarching goals by:  
- **Exploring** Orphic texts and their distinctive vocabulary.  
- **Comparing** Orphic themes with other poetic and philosophical traditions, such as Stoicism.  
- **Utilising** digital tools like **TF-IDF** to enhance textual analysis, showcasing how computational methods reveal patterns in historical texts.  

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
The following critical editions were consulted for the texts, via [TLG](https://stephanus.tlg.uci.edu/index.php):

1. T.W. Allen, W.R. Halliday, and E.E. Sikes, _The Homeric hymns_, 2nd edn., Oxford: Clarendon Press, 1936.
2. \[Anon.], "Der orphische Papyrus von Derveni," _Zeitschrift für Papyrologie und Epigraphik_ 47 (1982).
3. J.-M. Martin, _Arati phaenomena_, Florence: La Nuova Italia Editrice, 1956.
4. R. Pfeiffer, _Callimachus_, vol. 2, Oxford: Clarendon Press, 1953.
5. J.U. Powell, Collectanea Alexandrina, Oxford: Clarendon Press, 1925 (repr. 1970)
6. W. Quandt, _Orphei hymni_, 3rd edn., Berlin: Weidmann, 1962 (repr. 1973).

---

## Challenges, Ideas, and Future Work
1. **NLP Limitations**: The accuracy of lemmatisation and TF-IDF for Ancient Greek remains challenging.
2. **Phrases and Metre**: How does the analysis adapt to poetic metre and phrasing?
3. **Cross-Linguistic Comparison**: Results may differ significantly in Latin translations.
4. **Corpus Expansion**: Including texts from the Byzantine era (e.g., Gemistos Plethon) could add another dimension.

---

## Acknowledgements
This project connects to the **[VERITRACE](https://veritrace.eu)** project, and my ongoing PhD research focused on Stoic texts.

---

## License
This project is licensed under the MIT License.

