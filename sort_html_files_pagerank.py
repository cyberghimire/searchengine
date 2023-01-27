#168321

import networkx as nx

import glob

# specify the directory path and file extension
path = '/path/to/directory'
extension = '*.html'

# use the glob function to get a list of files
html_files = glob.glob(path + '/' + extension)

# print the list of files
print(files)


# Create an empty directed graph
G = nx.DiGraph()

# Add nodes (HTML files) to the graph
for html_file in html_files:
    G.add_node(html_file)

# Extract links from HTML files
for html_file in html_files:
    soup = BeautifulSoup(open(html_file), 'html.parser')
    for link in soup.find_all('a'):
        G.add_edge(html_file, link['href'])

# Calculate PageRank scores for each node
pr = nx.pagerank(G)

# Sort HTML files according to their PageRank scores
sorted_html_files = sorted(html_files, key=lambda x: pr[x], reverse=True)