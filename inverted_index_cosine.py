import os
import re
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def create_inverted_index(files_path):
    # Initialize an empty list to store the documents
    documents = []
    for file in os.listdir(files_path):
        # Open the file and extract the text
        with open(os.path.join(files_path, file), 'r', encoding='utf-8') as f:
            html = f.read()
            soup = BeautifulSoup(html, 'html.parser')
            text = soup.get_text()
            # Append the text to the list of documents
            documents.append(text)
    # Create a CountVectorizer object
    vectorizer = CountVectorizer()
    # Create the VSM of the documents
    vsm = vectorizer.fit_transform(documents)
    # Create an inverted index from the VSM
    inverted_index = vsm.transpose()
    # Create a mapping of terms to their index in the VSM
    terms = vectorizer.get_feature_names()
    term_index_map = {terms[i]: i for i in range(len(terms))}
    return inverted_index, term_index_map

def search_vsm(query, inverted_index, term_index_map):
    # Tokenize the query
    query_tokens = re.findall(r'\b\w+\b', query)
    # Create a vector for the query
    query_vector = [0] * len(term_index_map)
    for token in query_tokens:
        if token in term_index_map:
            query_vector[term_index_map[token]] = 1
    # Calculate the cosine similarity between the query vector and each document vector
    similarities = cosine_similarity(query_vector, inverted_index)
    # Convert the similarities to a DataFrame
    similarities_df = pd.DataFrame(similarities, columns=["Similarity"])
    # Return the index of the most similar document
    return similarities_df.idxmax()

if __name__ == '__main__':
    files_path = "html_files/"
    inverted_index, term_index_map = create_inverted_index(files_path)
    query = "Ghimire"
    result = search_vsm(query, inverted_index, term_index_map)
    print(f'Most similar document: {result}')
