import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Create a list of documents (websites)
documents = [
    "Hello, My name is aadarsha ghimire.",
    "Hello, My name is samikshya ghimire.",
    "Hello, My name is Shakuntala Nepal.",
    "Hello, My name is J.P. Ghimire"
]

# Create a Tf-Idf vectorizer
vectorizer = TfidfVectorizer()

# Create the vector space model
X = vectorizer.fit_transform(documents)

# Search a query in the vector space model
query = "ghimire"
query_vec = vectorizer.transform([query])

# Compute the cosine similarity between the query and all documents
similarities = cosine_similarity(query_vec, X)

print(similarities)

# Extract the relevance scores for each document
relevance_scores = similarities.flatten()
print(relevance_scores)

def is_full_of_zeros(arr):
    # Check if all elements of the array are 0
    return np.all(arr == 0)

if is_full_of_zeros(relevance_scores):
    print("Not found")
else:
    relevant_indices = np.nonzero(relevance_scores)[0]
    print(relevant_indices)

    # Rank the documents based on their relevance scores
    # ranked_indices = np.argsort(-relevant_indices)
    # print(ranked_indices)

    # Print the ranked documents
    for i in relevant_indices:
        print(f"Document {i+1} : {documents[i]}")
