def search(index, query):
    terms = query.split()
    results = set()
    for term in terms:
        if term in index:
            if not results:
                results = set(index[term])
            else:
                results = results.intersection(set(index[term]))
    if not results:
        print("No documents found.")
        return
    for doc_id in results:
        positions = []
        for term in terms:
            positions.append(index[term][doc_id])
        for i in range(len(positions[0])):
            found = True
            for j in range(1, len(positions)):
                if not positions[j] or i+j not in positions[j]:
                    found = False
                    break
            if found:
                print(f"Document {doc_id}: {' '.join(terms)} found at position {positions[0][i]}.")

pos_inv_index = {
    'the': {
        'doc1': [1, 6],
        'doc2': [1],
    },
    'quick': {
        'doc1': [2],
    },
    'brown': {
        'doc1': [3],
    },
    'fox': {
        'doc1': [4],
    },
    'jumped': {
        'doc1': [5],
    },
    'over': {
        'doc1': [6],
    },
    'lazy': {
        'doc1': [7],
        'doc2': [2],
    },
    'dog': {
        'doc1': [8],
        'doc2': [3],
    },
    'sat': {
        'doc2': [4],
    },
    'in': {
        'doc2': [5],
    },
    'shade': {
        'doc2': [6],
    },
    'of': {
        'doc2': [7],
    },
    'tree': {
        'doc2': [8],
    },
}

query = 'lazy dog'
search(pos_inv_index, query)
