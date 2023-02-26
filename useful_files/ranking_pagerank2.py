import networkx as nx
from bs4 import BeautifulSoup
import requests

urls = ['http://localhost:5000/a', 'http://localhost:5000/b', 'http://localhost:5000/c', 
            'http://localhost:5000/d', 'http://localhost:5000/e']
# Create an empty directed graph
G = nx.DiGraph()

# Add nodes (HTML files) to the graph
for url in urls:
    G.add_node(url)

# Extract links from HTML files
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a'):
        G.add_edge(url, link['href'])

# Calculate PageRank scores for each node
pr = nx.pagerank(G)

# Sort HTML files according to their PageRank scores
sorted_urls = sorted(urls, key=lambda x: pr[x], reverse=True)
print(sorted_urls)