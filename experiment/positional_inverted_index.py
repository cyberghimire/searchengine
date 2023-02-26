# Define a corpus of documents
corpus = {
    'doc1': 'the quick brown fox',
    'doc2': 'jumped over the lazy dog',
    'doc3': 'the quick brown fox jumped over the lazy dog',
    'doc4': 'the lazy dog slept'
}

# Define a function to tokenize a document
def tokenize(doc):
    return doc.split()

# Create an empty dictionary for the inverted index
inverted_index = {}

# Loop over each document in the corpus
for doc_id, doc in corpus.items():
    # Tokenize the document
    terms = tokenize(doc)
    # Loop over each term position in the document
    for position, term in enumerate(terms):
        # If the term is not already in the inverted index, add it
        if term not in inverted_index:
            inverted_index[term] = {}
        # If the document ID is not already in the inverted index for the term, add it with an empty list of positions
        if doc_id not in inverted_index[term]:
            inverted_index[term][doc_id] = []
        # Add the position to the inverted index for the term and document ID
        inverted_index[term][doc_id].append(position)

# Print the inverted index
for term, doc_positions in inverted_index.items():
    print('{}: {}'.format(term, doc_positions))
    # print("hello")
