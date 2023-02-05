import os
import networkx as nx
from bs4 import BeautifulSoup
import requests

# Extract links from HTML files
# html_files = ["A.html", "B.html", "C.html", "D.html", "E.html"]
# outgoing_links = {}
# for file in html_files:
#     with open(os.path.join("../html_files", file), 'r') as f:
#         soup = BeautifulSoup(f, 'html.parser')
#         links = [link.get('href') for link in soup.find_all('a') if link.get('href')]
#         outgoing_links[file] = links



def extract_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            links.append(href)
    return links

websites = ['localhost:5000/a', 'localhost:5000/b', 'localhost:5000/c', 'localhost:5000/d', 'localhost:5000/e']
all_links = {}
for website in websites:
    url = 'http://' + website
    links = extract_links(url)
    all_links[website] = links

# print(outgoing_links)

# Create a graph and add edges based on links
G = nx.DiGraph()
# for file, links in outgoing_links.items():
for file, links in all_links.items():
    G.add_node(file)
    for link in links:
        G.add_edge(file, link)

# Calculate PageRank, considering the edges as weight
pagerank = nx.pagerank(G, weight='weight')

# Sort files by PageRank and return top results
ranked_results = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)
top_results = ranked_results[:4]
print(ranked_results)