import os
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from bs4 import BeautifulSoup
import requests
from nltk.corpus import stopwords
import nltk

# Parse HTML files and extract text content
# html_files = ["../html_files/A.html", "../html_files/B.html", "../html_files/C.html", "../html_files/D.html", "../html_files/E.html"]
# text_content = []
# for file in html_files:
#     with open(file, 'r') as f:
#         soup = BeautifulSoup(f, 'html.parser')
#         text_content.append(soup.get_text())

# html_files = ["A.html", "B.html", "C.html", "D.html", "E.html"]
websites = ['localhost:5000/a', 'localhost:5000/b', 'localhost:5000/c', 'localhost:5000/d', 'localhost:5000/e']


# def extract_links(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     links = []
#     for link in soup.find_all('a'):
#         href = link.get('href')
#         if href:
#             links.append(href)
#     return links

# # outgoing_links = {}
# text_content = []
# for file in html_files:
#     with open(os.path.join("../html_files", file), 'r') as f:
#         soup = BeautifulSoup(f, 'html.parser')
#         # links = [link.get('href') for link in soup.find_all('a') if link.get('href')]
#         # outgoing_links[file] = links
#         text_content.append(soup.get_text())
text_content = []
for website in websites:
    url = 'http://' + website
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text_content.append(soup.get_text())
    

# nltk.download("stopwords")
# Tokenize and remove stop words
stop_words = set(stopwords.words("english"))
tokenized_text = []
for content in text_content:
    tokens = content.lower().split()
    tokenized_text.append([token for token in tokens if token not in stop_words])

# Calculate tf-idf
tfidf = TfidfVectorizer()
tfidf_vectors = tfidf.fit_transform([' '.join(tokens) for tokens in tokenized_text])

# Search using cosine similarity
query = "Peter"
query_vector = tfidf.transform([query])
similarities = cosine_similarity(query_vector, tfidf_vectors)


# Create a graph and add edges based on similarity scores
# G = nx.Graph()
G=nx.DiGraph()

for i, file in enumerate(websites):
    G.add_node(file)
    for j, sim in enumerate(similarities[0]):
        if sim > 0 and i != j:
            G.add_edge(file, websites[j], weight=sim)

# for file, links in outgoing_links.items():
#     G.add_node(file)
#     for link in links:
#         G.add_edge(file, link)

# for file, links in outgoing_links.items():
#     G.add_node(file)
#     for j, sim in enumerate(similarities[0]):
#         if sim > 0 and i != j:
#             G.add_edge(file, html_files[j], weight=sim)

# Calculate PageRank
pagerank = nx.pagerank(G, weight = 'weight')

# Sort files by PageRank and return top results
ranked_results = sorted(pagerank.items(), key=lambda x: x[1], reverse=False)

# top_results = ranked_results[:3]
top_results = [x[0] for x in ranked_results if x[1]>0.14]
# results = dict((x) for x, y in top_results)
print(top_results)