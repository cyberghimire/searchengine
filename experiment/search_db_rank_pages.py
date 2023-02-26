import sqlite3
import networkx as nx
from bs4 import BeautifulSoup

def search_database(query):
    # Connect to the SQLite database
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
    results.sort(key=lambda x: x[1], reverse=True)

    # Print the search results
    for result in results:
        print(result[0])

    # Close the database connection
    conn.close()


search_database("Donald Trump")