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
    # Loop over each term in the document
    for term in terms:
        # If the term is not already in the inverted index, add it
        if term not in inverted_index:
            inverted_index[term] = []
        # Add the document ID to the inverted index for the term
        inverted_index[term].append(doc_id)

# Print the inverted index
for term, doc_ids in inverted_index.items():
    print('{}: {}'.format(term, doc_ids))