import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

#list of websites
websites = ["http://www.example1.com", "http://www.example2.com", "http://www.example3.com"]

#list of website contents
contents = ["website1", "content of website 2", "content of website 3"]

# create a dataframe
df = pd.DataFrame({'websites': websites, 'contents': contents})

#define query
query = "website1"

# Tokenize the contents
df['tokens'] = df['contents'].apply(word_tokenize)

# Remove stop words
stop_words = set(stopwords.words('english'))
df['tokens'] = df['tokens'].apply(lambda x: [item for item in x if item.lower() not in stop_words])

# Perform TF-IDF on the tokenized contents
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform([' '.join(x) for x in df['tokens']])

# Get the feature names
feature_names = tfidf.get_feature_names()

# Get the TF-IDF score for the query
query_vector = tfidf.transform([query])

# Find the index of the query in the feature names
query_index = feature_names.index(query)

# Get the TF-IDF scores for the query for each website
scores = tfidf_matrix.getcol(query_index).toarray()

# Create a new column in the dataframe with the scores
df['relevancy_score'] = scores

# Sort the dataframe by relevancy score
df = df.sort_values('relevancy_score', ascending=False)

# Print the relevancy scores
print(df[['websites','relevancy_score']])
