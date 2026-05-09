# Information Retrieval in Nepal Bhasa (Newari)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Low Resource NLP](https://img.shields.io/badge/NLP-Low--Resource-green.svg)]()

This repository contains the implementation of a standardized Information Retrieval (IR) benchmark for **Nepal Bhasa (Newari)**, a Sino-Tibetan language classified by UNESCO as "definitely endangered." This project addresses the lack of digital search infrastructure for the language using a combination of custom linguistic engineering and modern transformer-based dense retrieval.

---

## 🚀 Key Features

*   **Curated Corpus:** A 80,000-document corpus aggregated from Nepal Mandal (50%) and Wikipedia (50%).
*   **Custom Preprocessing:** Devanagari-specific normalization and a Snowball-inspired rule-based stemmer.
*   **Hybrid Retrieval:** Comparative evaluation of traditional sparse methods (TF-IDF) and modern dense embeddings.
*   **Fine-tuned Models:** State-of-the-art results using domain-adapted **MuRIL** and **Alibaba GTE** models.
*   **Cross-Lingual Support:** Evaluation of Newari-to-English retrieval capabilities.

---

## 📊 Experimental Results

Evaluated using 1,000 manually annotated query-document pairs, dense retrieval models consistently outperformed lexical baselines.

### Nepal Bhasa IR Performance
| Model | MRR | MAP | Recall@10 | Acc@1 |
| :--- | :--- | :--- | :--- | :--- |
| **TF-IDF (Baseline)** | 0.5678 | 0.5678 | 0.6767 | 0.5067 |
| **Google mBERT** | 0.7515 | 0.7515 | 0.8300 | 0.7100 |
| **Alibaba GTE** | 0.8006 | 0.8006 | 0.8867 | 0.7333 |
| **Further Tuned MuRIL** | **0.8321** | **0.8321** | **0.8933** | **0.7900** |

### Cross-Lingual Alignment (Newari → English)
Using intermediate **Masked Language Modeling (MLM)** on the Nepal Bhasa corpus significantly reduced the alignment gap.

| Task | MRR | MAP | Recall@10 |
| :--- | :--- | :--- | :--- |
| English-English (Baseline) | 0.4159 | 0.0431 | 0.0669 |
| Newari-English (MLM-Enhanced) | 0.2682 | 0.0335 | 0.0679 |

---

## 🛠️ Methodology

### 1. Data Pipeline
*   **Normalization:** Unicode standardization using NFC composition for Devanagari script.
*   **Stemming:** Rule-based suffix stripping for nominal and verbal inflections (case, tense, aspect).
*   **Stopwords:** Frequency-derived and manually verified list of high-frequency functional words.

### 2. Training Strategy
*   **Stage 1 (MLM):** Continued pre-training on 80k documents for domain-specific linguistic knowledge.
*   **Stage 2 (Contrastive Learning):** Fine-tuning with **InfoNCE loss** using hard negative sampling (selected via BM25).

---

## 💻 Tech Stack & Requirements

### Software Specifications
*   **Language:** Python 3.10+
*   **Frameworks:** PyTorch 2.0+, Hugging Face Transformers 4.30+
*   **Libraries:** FAISS, NLTK, spaCy, Pandas, Scikit-learn

### Hardware Requirements
*   **GPU:** NVIDIA RTX 3060 (12GB VRAM); RTX 3090 recommended for training.
*   **RAM:** 16GB minimum (32GB recommended).