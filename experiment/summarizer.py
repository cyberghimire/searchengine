import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from heapq import nlargest

def summarize(text, n):
    # tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # tokenize the sentences into words and remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in word_tokenize(text.lower()) if word.isalpha() and word not in stop_words]
    
    # create a frequency distribution of the words
    freq_dist = nltk.FreqDist(words)
    
    # calculate the score of each sentence by adding up the frequency of its words
    scores = {}
    for i, sentence in enumerate(sentences):
        words = [word for word in word_tokenize(sentence.lower()) if word.isalpha() and word not in stop_words]
        score = sum([freq_dist[word] for word in words])
        scores[i] = score
    
    # select the top n sentences with the highest scores
    indexes = nlargest(n, scores, key=scores.get)
    summary = [sentences[i] for i in sorted(indexes)]
    
    # join the selected sentences into a single string and return it
    return ' '.join(summary)

text = """
The Bhagavata Purana, like other puranas, discusses a wide range of topics including cosmology, astronomy, genealogy, geography, legend, music, dance, yoga and culture. As it begins, the forces of evil have won a war between the benevolent devas (deities) and evil asuras (demons) and now rule the universe. Truth re-emerges as Krishna, (called "Hari" and "Vāsudeva" in the text) first makes peace with the demons, understands them and then creatively defeats them, bringing back hope, justice, freedom and happiness – a cyclic theme that appears in many legends.

The Bhagavata Purana is a revered text in Vaishnavism, a Hindu tradition that reveres Vishnu. The text presents a form of religion (dharma) that competes with that of the Vedas, wherein bhakti ultimately leads to self-knowledge, salvation (moksha) and bliss. However the Bhagavata Purana asserts that the inner nature and outer form of Krishna is identical to the Vedas and that this is what rescues the world from the forces of evil. An oft-quoted verse is used by some Krishna sects to assert that the text itself is Krishna in literary form.

The date of composition is probably between the eighth and the tenth century CE, but may be as early as the 6th century CE. Manuscripts survive in numerous inconsistent versions revised through the 18th century creating various recensions both in the same languages and across different Indian languages.
"""

summary = summarize(text, 3)
print(summary)

