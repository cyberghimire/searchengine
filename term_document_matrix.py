# import requests
# from bs4 import BeautifulSoup
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from sklearn.feature_extraction.text import CountVectorizer

# # Function to get text from website
# def get_text(url):
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     text = soup.get_text()
#     return text

# # Function to convert text to document-term matrix
# def text_to_dtm(text):
#     # Tokenize text
#     tokens = word_tokenize(text)
#     # Remove stop words
#     stop_words = set(stopwords.words('english'))
#     filtered_tokens = [w for w in tokens if w.lower() not in stop_words]
#     # Convert list of words to list of strings
#     text = [" ".join(filtered_tokens)]
#     # Create the Document-Term matrix
#     count_vectorizer = CountVectorizer(ngram_range=(1,1))
#     sparse = count_vectorizer.fit_transform(text)
#     dtm = sparse
#     return dtm

# # Example usage
# url = "https://en.wikipedia.org/wiki/MTorrent"
# text = get_text(url)
# dtm = text_to_dtm(text)
# print(dtm)


import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize

# Function to get text from website
def get_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.get_text()
    return text

# Function to create the inverted index
def create_inverted_index(text):
    # Tokenize text
    tokens = word_tokenize(text)
    # Create the inverted index
    inverted_index = {}
    for i, token in enumerate(tokens):
        if token not in inverted_index:
            inverted_index[token] = []
        inverted_index[token].append(i)
    return inverted_index

# Example usage
url = "https://en.wikipedia.org/wiki/MTorrent"
text = get_text(url)
inverted_index = create_inverted_index(text)
print(inverted_index)




# Function to search the inverted index
def search_inverted_index(query):
    query_tokens = query.split()
    result = None
    for token in query_tokens:
        if token in inverted_index:
            if result is None:
                result = set(inverted_index[token])
            else:
                result = result.intersection(inverted_index[token])
    return result

# Example usage
query = "free"
result = search_inverted_index(query)
print(result)