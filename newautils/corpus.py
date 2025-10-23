from pathlib import Path
import pandas as pd


def build_corpus_csv(folder_path, output_path):

    folder_path = Path(folder_path)

    files = list(folder_path.glob("*"))

    corpus = pd.DataFrame({
        "filename": [f.name for f in files],
        # "text": [f.read_text(encoding="utf-8").replace("\n", " ") for f in files]
        "text": [f.read_text(encoding="utf-8") for f in files]
    })

    corpus.to_csv(output_path, index=False)


def compute_term_frequency(documents):
    from collections import Counter
    import tokenizer

    term_frequency = Counter()
    for document in documents:
        term_frequency.update(tokenizer.tokenize(document))

    # return term_frequency.most_common()
    return sorted(term_frequency.items(), key=lambda x: x[0])

