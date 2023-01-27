import os
import networkx as nx
from bs4 import BeautifulSoup

# Extract links from HTML files
html_files = ["A.html", "B.html", "C.html", "D.html", "E.html"]
outgoing_links = {}
for file in html_files:
    with open(os.path.join("html_files", file), 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        links = [link.get('href') for link in soup.find_all('a') if link.get('href')]
        outgoing_links[file] = links

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