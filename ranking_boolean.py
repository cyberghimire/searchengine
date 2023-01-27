from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# Create a list of documents (websites)
documents = [
    "website1 content",
    "website2 content",
    "website3 content",
    "website4 content"
]

# Create a Count vectorizer
vectorizer = CountVectorizer(binary=True)

# Create the vector space model
X = vectorizer.fit_transform(documents)

# Search a query in the vector space model
query = "website3"
query_vec = vectorizer.transform([query])

# Get the indices of the documents that contain the query terms
# We use the boolean AND operation (query_vec & X)
# This will return a sparse matrix with only the documents where all the query terms are present
# Then we convert the sparse matrix to dense array and get the non zero indices
matching_docs_indices = np.nonzero(query_vec.toarray() & X.toarray())[1]

# Initialize relevance scores with 0
relevance_scores = np.zeros(len(documents))

# For each matching document, increase the relevance score by 1
for i in matching_docs_indices:
    relevance_scores[i] += 1

# Rank the documents based on their relevance scores
ranked_indices = np.argsort(-relevance_scores)

# Print the ranked documents
for i in ranked_indices:
    print(f"Document {i+1} : {documents[i]}")
