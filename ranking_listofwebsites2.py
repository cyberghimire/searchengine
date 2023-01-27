import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Create a list of documents (websites)
documents = [
    "website1 content",
    "website2 content",
    "website3 content",
    "website4 content"
]

# Create a Tf-Idf vectorizer
vectorizer = TfidfVectorizer()

# Create the vector space model
X = vectorizer.fit_transform(documents)

# Search a query in the vector space model
query = "website2"
query_vec = vectorizer.transform([query])

# Compute the cosine similarity between the query and all documents
similarities = cosine_similarity(query_vec, X)

# Extract the relevance scores for each document
relevance_scores = similarities.flatten()

# Create a graph of the websites
G = nx.DiGraph()
G.add_nodes_from(range(len(documents)))

# Add edges to the graph based on the relevance scores
for i in range(len(documents)):
    for j in range(len(documents)):
        if i != j and relevance_scores[i] > 0:
            G.add_edge(i, j, weight=relevance_scores[i])

# Compute the PageRank of the websites
pageranks = nx.pagerank(G)

# Sort the websites based on their PageRank
sorted_pageranks = sorted(pageranks.items(), key=lambda x: x[1], reverse=False)

# Print the ranked websites
for i, pagerank in sorted_pageranks:
    print(f"Website {i+1} : {documents[i]}")
