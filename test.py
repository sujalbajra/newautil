import newautils
import pandas as pd

corpus = pd.read_csv('data/corpus.csv')

tfidf_matrix, vectorizer = newautils.compute_tfidf(corpus)

output = newautils.vsm.search("नेपाल भारतया", tfidf_matrix, vectorizer, top_k=3)

for docid, score in output:
    print("Document id: " + str(docid) + " with score " + str(score) + "\n")
    print(corpus['text'].iloc[docid])
    print("\n----------------\n")
