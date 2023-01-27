import networkx as nx

# Create an empty directed graph
G = nx.DiGraph()

# Add edges to the graph representing the links between websites
websites = ["A", "B", "C", "D"]
for website in websites:
    G.add_node(website)

G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("C", "A")
G.add_edge("D", "C")

# Calculate the PageRank of the websites
pr = nx.pagerank(G)

sorted_pr = sorted(pr.items(), key=lambda x: x[1], reverse=True)

# Print the websites in descending order of PageRank score
for website, rank in sorted_pr:
    print(website, rank)
