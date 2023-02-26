import sqlite3
import requests
from bs4 import BeautifulSoup

def bfs_crawler(start_url, max_pages=100):
    # Connect to the SQLite database
    conn = sqlite3.connect('crawler.db')
    c = conn.cursor()

    # Create the table to store the crawled pages, if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS pages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE,
            content TEXT
        )
    ''')
    conn.commit()

    # Initialize the queue with the starting URL
    queue = [start_url]
    # queue = start_url

    # Initialize a set to keep track of visited pages
    visited = set()

    # Keep crawling until the queue is empty or we reach the maximum number of pages
    while queue and len(visited) < max_pages:
        # Get the next URL from the queue
        url = queue.pop(0)

        # Skip this page if we've already visited it
        if url in visited:
            continue

        # Print the URL we're about to crawl
        print(f"Crawling {url}")

        # Make a GET request to the URL
        response = requests.get(url)

        # Skip this page if there was an error
        if response.status_code != 200:
            continue

        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Save the page content to the database
        c.execute('INSERT OR IGNORE INTO pages (url, content) VALUES (?, ?)', (url, str(soup)))
        conn.commit()

        # Add any links on the page to the queue
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            if href and 'http' in href and href not in visited:
                queue.append(href)

        # Mark the current page as visited
        visited.add(url)

    # Close the database connection
    conn.close()

    # Print a message indicating that crawling is complete
    print("Crawling complete.")


url_frontier = ['https://www.bbc.com', 'https://www.cnn.com']
for url in url_frontier:
    bfs_crawler(url, 50)
