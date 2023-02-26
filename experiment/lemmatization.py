import nltk
from nltk.stem import WordNetLemmatizer

# Example words
sentence = "the bats were hanging by their feet"
# Perform lemmatization

words = nltk.word_tokenize(sentence)

lemmatizer = WordNetLemmatizer()

lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

# Print the lemmatized words
print(lemmatized_words)