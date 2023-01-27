import requests
from bs4 import BeautifulSoup
import os

def crawl_sitemap(url):
    # Send a GET request to the sitemap URL
    response = requests.get(url)
    # Parse the sitemap XML
    soup = BeautifulSoup(response.content, 'xml')
    # Extract the URLs of the pages in the sitemap
    pages = [loc.text for loc in soup.find_all('loc')]

    # Iterate through the URLs, retrieve the HTML of each page, and store it locally
    for page in pages:
        # Send a GET request to the page URL
        response = requests.get(page)
        # Extract the HTML of the page
        html = response.content
        # Create a file name for the page
        filename = page.replace("/", "_") + ".html"
        # Write the HTML to the file
        with open(filename, 'wb') as f:
            f.write(html)
            print(f"{filename} has been created")

if __name__ == "__main__":
    sitemap_url = "https://www.example.com/sitemap.xml"
    crawl_sitemap(sitemap_url)
