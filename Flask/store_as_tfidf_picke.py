import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from bs4 import BeautifulSoup
import requests

def save_tokenized_text(tokenized_text, filename):
    with open(filename, 'wb') as f:
        pickle.dump(tokenized_text, f)

def load_tokenized_text(filename):
    with open(filename, 'rb') as f:
        vectorized_docs = pickle.load(f)
    return vectorized_docs

if not os.path.exists('tokenized_text.pkl'):
    # corpus = [
    #     "The quick brown fox jumps over the lazy dog.",
    #     "A quick brown dog outpaces a quick fox.",
    #     "The lazy dog is quick to jump over the brown fox."
    # ]

    websites = ['http://localhost:5000/a', 'http://localhost:5000/b', 'http://localhost:5000/c', 'http://localhost:5000/d', 'http://localhost:5000/e']
    text_content = []
    for website in websites:
        # url = 'http://' + website
        response = requests.get(website)
        soup = BeautifulSoup(response.text, 'html.parser')
        text_content.append(soup.get_text())
    stop_words = ['the', 'is', 'and', 'to', 'of', 'a', 'in', 'that', 'for', 'it']
    tokenized_text = []
    for content in text_content:
        tokens = content.lower().split()
        tokenized_text.append([token for token in tokens if token not in stop_words])

    # tfidf = TfidfVectorizer()
    # vectorized_docs = tfidf.fit_transform([' '.join(tokens) for tokens in tokenized_text])
    print(tokenized_text)
    save_tokenized_text(tokenized_text, 'tokenized_text.pkl')
else:
    vectorized_docs = load_tokenized_text('tokenized_text.pkl')
