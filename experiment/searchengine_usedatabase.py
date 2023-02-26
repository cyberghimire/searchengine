from flask import Flask, render_template, request
import pickle
import os
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from bs4 import BeautifulSoup
import requests
import sqlite3

app = Flask(__name__, template_folder="../html_files/", static_folder="../html_files/images")

@app.route("/")
def search():
    return render_template('search.html')

# @app.route("/a")
# def a():
#     return render_template('A.html')

# @app.route("/b")
# def b():
#     return render_template('B.html')

# @app.route("/c")
# def c():
#     return render_template('C.html')

# @app.route("/d")
# def d():
#     return render_template('D.html')

# @app.route("/e")
# def e():
#     return render_template('E.html')


# def load_tokenized_text(filename):
#     tokenized_text = pickle.load(open(filename, 'rb'))
#     return tokenized_text



@app.route("/search", methods = ['GET','POST'])
def searchx():
    if request.method == 'POST':
        query = request.form['query']
        if query=="":
            return render_template("search.html")
        
        # websites = ['http://localhost:5000/a', 'http://localhost:5000/b', 
        #             'http://localhost:5000/c', 'http://localhost:5000/d', 'http://localhost:5000/e']
  

        # # # Calculate tf-idf
        # tokenized_text = load_tokenized_text('tokenized_text.pkl')
        # tfidf = TfidfVectorizer()
        # tfidf_vectors = tfidf.fit_transform([' '.join(tokens) for tokens in tokenized_text])

       
        
        # # Search using cosine similarity

        # query_vector = tfidf.transform([query])
        # similarities = cosine_similarity(query_vector, tfidf_vectors)

        # if all_zeros(similarities[0]):
        #     return render_template("notfound.html")

        # # Create a graph and add edges based on similarity scores
        # G=nx.DiGraph()

        # for i, link in enumerate(websites):
        #     G.add_node(link)
        #     for j, sim in enumerate(similarities[0]):
        #         if sim > 0 and i != j:
        #             # G.add_edge(file, websites[j], weight=sim)
        #             G.add_edge(link, websites[j])


        # # Calculate PageRank
        # # pagerank = nx.pagerank(G, weight = 'weight')
        # pagerank = nx.pagerank(G)

        # # Sort files by PageRank and return top results
        # ranked_results = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)

        # top_results = [x[0] for x in ranked_results if x[1]>=0.14]

        conn = sqlite3.connect('crawler.db')
        c = conn.cursor()

        # Query the database for pages that contain the search term
        c.execute("SELECT id, url, content FROM pages WHERE content LIKE ?", ('%' + query + '%',))
        rows = c.fetchall()

        # Create a directed graph to represent the links between pages
        G = nx.DiGraph()

        # Add nodes to the graph for each page
        for row in rows:
            id, url, content = row
            G.add_node(url)

        # Add edges to the graph for each link between pages
        c.execute("SELECT id, url, content FROM pages")
        all_rows = c.fetchall()
        for row in all_rows:
            id, url, content = row
            soup = BeautifulSoup(content, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                href = link.get('href')
                if href and 'http' in href:
                    G.add_edge(url, href)

        # Calculate the PageRank for each page in the graph
        pr = nx.pagerank(G)

        # Sort the search results by PageRank
        results = [(url, pr[url]) for url in pr if url in [row[1] for row in rows]]
        results.sort(key=lambda x: x[1], reverse=False)

        return render_template('results.html', data=results)


def all_zeros(lst):
    for i in lst:
        if i != 0:
            return False
    return True


if __name__ == '__main__':
    app.run(debug=True)