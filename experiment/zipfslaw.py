import nltk
import matplotlib.pyplot as plt
from collections import Counter

nltk.download('brown')

# Load the Brown corpus from NLTK
words = nltk.corpus.brown.words()

# Count the frequency of each word
word_freq = Counter(words)

# Sort the words by frequency
sorted_words = sorted(word_freq, key=word_freq.get, reverse=True)

# Plot the frequency of the top 50 words
x = range(50)
y = [word_freq[sorted_words[i]] for i in range(50)]
plt.plot(x, y)
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.title('Zipf\'s Law')
plt.show()
