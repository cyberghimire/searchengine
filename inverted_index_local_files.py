import os
from bs4 import BeautifulSoup
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

def create_inverted_index(files):
    # Create an empty dictionary to store the inverted index
    inverted_index = {}
    
    # Read the content of each file
    for file in files:
        with open(os.path.join("html_files/", file), 'r') as f:
            html = f.read()
            # Use BeautifulSoup to parse the HTML and extract the text
            soup = BeautifulSoup(html, 'html.parser')
            text = soup.get_text()
            # Tokenize the text
            tokens = text.split()
            # Iterate through the tokens and add them to the inverted index
            for token in tokens:
                if token in inverted_index:
                    inverted_index[token].append(file)
                else:
                    inverted_index[token] = [file]
    return inverted_index

def search_inverted_index(inverted_index, query):
    # Tokenize the query
    query_tokens = query.split()
    # Create a set of documents that contain at least one of the query tokens
    relevant_docs = set()
    for token in query_tokens:
        if token in inverted_index:
            relevant_docs.update(inverted_index[token])
    return relevant_docs

def vector_space_model(files, query):
    inverted_index = create_inverted_index(files)
    relevant_docs = search_inverted_index(inverted_index, query)
    data = []
    for file in files:
        with open(os.path.join("html_files/", file), 'r') as f:
            html = f.read()
            soup = BeautifulSoup(html, 'html.parser')
            text = soup.get_text()
            data.append(text)
    df = pd.DataFrame({'document': data, 'relevant': [1 if file in relevant_docs else 0 for file in files]})
    count = CountVectorizer()
    count_matrix = count.fit_transform(df['document'])
    similarity = cosine_similarity(count_matrix)
    return df, similarity

if __name__ == '__main__':
    files = ['A.html', 'B.html', 'C.html', 'D.html', 'E.html', 'F.html']
    query = 'Ghimire'
    df, similarity = vector_space_model(files, query)
    print(df)
    print(similarity)
