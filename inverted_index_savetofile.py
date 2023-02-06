import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

def save_vectorized_documents(vectorized_docs, filename):
    with open(filename, 'wb') as f:
        pickle.dump(vectorized_docs, f)

def load_vectorized_documents(filename):
    with open(filename, 'rb') as f:
        vectorized_docs = pickle.load(f)
    return vectorized_docs

if not os.path.exists('tfidf_vectors.pkl'):
    corpus = [
        "The quick brown fox jumps over the lazy dog.",
        "A quick brown dog outpaces a quick fox.",
        "The lazy dog is quick to jump over the brown fox."
    ]

    tfidf_vectorizer = TfidfVectorizer()
    vectorized_docs = tfidf_vectorizer.fit_transform(corpus)
    save_vectorized_documents(vectorized_docs, 'tfidf_vectors.pkl')
else:
    vectorized_docs = load_vectorized_documents('tfidf_vectors.pkl')
    print(vectorized_docs)
