# Define an inverted index
inv_index = {
    'the': {'doc1', 'doc2', 'doc3', 'doc4'},
    'quick': {'doc1', 'doc2', 'doc4'},
    'brown': {'doc1', 'doc2', 'doc3'},
    'fox': {'doc1', 'doc4'},
    'jumped': {'doc2'},
    'over': {'doc2', 'doc3'},
    'lazy': {'doc3', 'doc4'},
    'dog': {'doc4'},
}

# Define a function to perform boolean retrieval
def boolean_retrieval(query):
    tokens = query.split()
    if len(tokens) == 1:
        return inv_index.get(tokens[0], set())
    else:
        if tokens[0] == 'NOT':
            return set(inv_index.keys()) - inv_index.get(tokens[1], set())
        elif tokens[1] == 'AND':
            return inv_index.get(tokens[0], set()).intersection(inv_index.get(tokens[2], set()))
        elif tokens[1] == 'OR':
            return inv_index.get(tokens[0], set()).union(inv_index.get(tokens[2], set()))
        else:
            raise ValueError('Invalid query')

# Example usage
query1 = 'quick AND jumped'
query2 = 'jumped OR over'
query3 = 'lazy AND NOT dog'
print(boolean_retrieval(query1))
print(boolean_retrieval(query2))
print(boolean_retrieval(query3))
