import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to get text from website
def get_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.get_text()
    return text

# Function to create the term-frequency inverse-document-frequency (tf-idf) matrix
def create_tfidf_matrix(texts):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(texts)
    return tfidf_matrix, tfidf_vectorizer

# Function to search the query in the vector space model
def search_query(query, tfidf_matrix, tfidf_vectorizer):
    query_vector = tfidf_vectorizer.transform([query])
    similarities = cosine_similarity(query_vector, tfidf_matrix)
    return similarities

# Example usage
#Get the text of the website
url = "https://en.wikipedia.org/wiki/MTorrent"
text = get_text(url)
texts = [text]
tfidf_matrix, tfidf_vectorizer = create_tfidf_matrix(texts)
query = "μTorrent"
similarities = search_query(query, tfidf_matrix, tfidf_vectorizer)
# get the index of the website with the highest similarity score
index = similarities.argmax()
print("The relevance score of the website is ", similarities[0][index])

