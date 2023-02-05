from flask import Flask, render_template, request


import os
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from bs4 import BeautifulSoup
import requests

app = Flask(__name__, template_folder="../html_files/")

@app.route("/")
def search():
    return render_template('search.html')

@app.route("/a")
def a():
    return render_template('A.html')

@app.route("/b")
def b():
    return render_template('B.html')

@app.route("/c")
def c():
    return render_template('C.html')

@app.route("/d")
def d():
    return render_template('D.html')

@app.route("/e")
def e():
    return render_template('E.html')

data = []

@app.route("/result")
def result():
    return render_template('results.html', data=data)

query = ""
text_content = []
@app.route("/search", methods = ['GET','POST'])
def searchx():
    if request.method == 'POST':
        query = request.form['query']
        if query=="":
            return render_template("search.html")
        websites = ['http://localhost:5000/a', 'http://localhost:5000/b', 'http://localhost:5000/c', 'http://localhost:5000/d', 'http://localhost:5000/e']
        text_content = []
        for website in websites:
            # url = 'http://' + website
            response = requests.get(website)
            soup = BeautifulSoup(response.text, 'html.parser')
            text_content.append(soup.get_text())
        stop_words = ['the', 'is', 'and', 'to', 'of', 'a', 'in', 'that', 'for', 'it']
        tokenized_text = []
        for content in text_content:
            tokens = content.lower().split()
            tokenized_text.append([token for token in tokens if token not in stop_words])

        # Calculate tf-idf
        tfidf = TfidfVectorizer()
        tfidf_vectors = tfidf.fit_transform([' '.join(tokens) for tokens in tokenized_text])

        # Search using cosine similarity
        # query = "Aadarsha"
        query_vector = tfidf.transform([query])
        similarities = cosine_similarity(query_vector, tfidf_vectors)


        # Create a graph and add edges based on similarity scores
        # G = nx.Graph()
        G=nx.DiGraph()

        for i, file in enumerate(websites):
            G.add_node(file)
            for j, sim in enumerate(similarities[0]):
                if sim > 0 and i != j:
                    G.add_edge(file, websites[j], weight=sim)

        # for file, links in outgoing_links.items():
        #     G.add_node(file)
        #     for link in links:
        #         G.add_edge(file, link)

        # for file, links in outgoing_links.items():
        #     G.add_node(file)
        #     for j, sim in enumerate(similarities[0]):
        #         if sim > 0 and i != j:
        #             G.add_edge(file, html_files[j], weight=sim)

        # Calculate PageRank
        pagerank = nx.pagerank(G, weight = 'weight')

        # Sort files by PageRank and return top results
        ranked_results = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)

        # top_results = ranked_results[:3]
        top_results = [x[0] for x in ranked_results if x[1]>0.2]

        if len(top_results) == 0:
            return render_template("notfound.html")
        return render_template('results.html', data=top_results)


if __name__ == '__main__':
    app.run(debug=True)