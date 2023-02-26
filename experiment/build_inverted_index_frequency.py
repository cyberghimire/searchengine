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
    # Loop over each term in the document
    for term in terms:
        # If the term is not already in the inverted index, add it with frequency 1
        if term not in inverted_index:
            inverted_index[term] = {}
            inverted_index[term][doc_id] = 1
        # If the term is already in the inverted index, increment the frequency for the document
        else:
            if doc_id not in inverted_index[term]:
                inverted_index[term][doc_id] = 1
            else:
                inverted_index[term][doc_id] += 1

# Print the inverted index with frequency
for term, doc_freq in inverted_index.items():
    print('{}: {}'.format(term, doc_freq))
