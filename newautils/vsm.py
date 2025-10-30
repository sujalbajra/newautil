from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
from . import tokenizer


def compute_tfidf(corpus):
    vectorizer = TfidfVectorizer( tokenizer=tokenizer.tokenize, token_pattern=None, use_idf=True, sublinear_tf=True)

    tfidf_matrix = vectorizer.fit_transform(corpus["text"].tolist())

    return tfidf_matrix, vectorizer


def build_inverted_index(tfidf_matrix, vectorizer):
    coo = tfidf_matrix.tocoo()
    inverted_index = defaultdict(list)
    terms = vectorizer.get_feature_names_out()

    for docid, termid, weight in zip(coo.row, coo.col, coo.data):
        inverted_index[terms[termid]].append((docid, weight))

    for postings in inverted_index.values():
        postings.sort(key=lambda x: x[1], reverse=True)

    return inverted_index


def search(query, tfidf_matrix, vectorizer, top_k=10):
    query_vector = vectorizer.transform([query])
    similarities = cosine_similarity(query_vector, tfidf_matrix)[0]
    top_indices = similarities.argsort()[-top_k:][::-1]
    return [(idx, similarities[idx]) for idx in top_indices]

import pickle
import scipy.sparse as sp

def load_tfidf_model(matrix_path="models/tfidf_matrix.npz", vectorizer_path="models/vectorizer.pkl"):
    tfidf_matrix = sp.load_npz(matrix_path)

    with open(vectorizer_path, "rb") as f:
        vectorizer = pickle.load(f)
    
    return tfidf_matrix, vectorizer
