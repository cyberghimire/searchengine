import os
import requests
from bs4 import BeautifulSoup

def bfs_crawler(start_url, max_pages=20):
    # Create a directory to store the crawled pages
    if not os.path.exists('pages'):
        os.mkdir('pages')

    # Initialize the queue with the starting URL
    queue = [start_url]

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

        # Save the page content to a local file
        page_path = os.path.join(r'pages', url.replace('http://', '').replace('https://', '').replace('/', '')
        .replace('&', '').replace('=', '').replace('?', '') + '.html')
        with open(page_path, 'w', encoding="utf-8") as f:
            f.write(str(soup))

        # Add any links on the page to the queue
        links = soup.find_all('a')
            
        for link in links:
            link = link.get("href")
            if link[0:1] == "/":
                link = url +link
            if link[0:1] == "#":
                continue
            href = link.get('href')
            if href and 'http' in href and href not in visited:
                queue.append(href)

        # Mark the current page as visited
        visited.add(url)

    # Print a message indicating that crawling is complete
    print("Crawling complete.")


bfs_crawler("http://www.bbc.com")
