import os
import networkx as nx
from bs4 import BeautifulSoup
import requests

# Extract links from HTML files
urls = ["http://localhost:5000/a", "http://localhost:5000/b", "http://localhost:5000/c", "http://localhost:5000/d", "http://localhost:5000/e"]
outgoing_links = {}
for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [link.get('href') for link in soup.find_all('a') if link.get('href')]
        outgoing_links[url] = links

# Create a graph and add edges based on links
G = nx.DiGraph()
for file, links in outgoing_links.items():
    G.add_node(file)
    for link in links:
        G.add_edge(file, link)

# Calculate PageRank, considering the edges as weight
pagerank = nx.pagerank(G, weight='weight')

# Sort files by PageRank and return top results
ranked_results = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)
top_results = ranked_results[:4]
print(ranked_results)