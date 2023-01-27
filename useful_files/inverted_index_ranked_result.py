import os
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from bs4 import BeautifulSoup

# Parse HTML files and extract text content
html_files = ["html_files/A.html", "html_files/B.html", "html_files/C.html", "html_files/D.html", "html_files/E.html"]
text_content = []
for file in html_files:
    with open(file, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        text_content.append(soup.get_text())

# Tokenize and remove stop words
stop_words = ['the', 'is', 'and', 'to', 'of', 'a', 'in', 'that', 'for', 'it']
tokenized_text = []
for content in text_content:
    tokens = content.lower().split()
    tokenized_text.append([token for token in tokens if token not in stop_words])

# Calculate tf-idf
tfidf = TfidfVectorizer()
tfidf_vectors = tfidf.fit_transform([' '.join(tokens) for tokens in tokenized_text])

# Search using cosine similarity
query = "Ghimire"
query_vector = tfidf.transform([query])
similarities = cosine_similarity(query_vector, tfidf_vectors)

# Create a graph and add edges based on similarity scores
G = nx.Graph()
for i, file in enumerate(html_files):
    G.add_node(file)
    for j, sim in enumerate(similarities[0]):
        if sim > 0 and i != j:
            G.add_edge(file, html_files[j], weight=sim)

# Calculate PageRank
pagerank = nx.pagerank(G)

# Sort files by PageRank and return top results
ranked_results = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)
top_results = ranked_results[:3]
print(top_results)
