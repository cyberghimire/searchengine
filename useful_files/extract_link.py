import requests
from bs4 import BeautifulSoup

# Set the URL of the webpage that you want to crawl
url = "https://www.bbc.com"


def getlinks(url):
    visited_links = set()
    # Download the HTML of the webpage
    response = requests.get(url)
    html = response.text

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Find all links in the HTML
    links = soup.find_all("a")


    # Print the links
    for link in links:
        link = link.get("href")
        if link[0:1] == "/":
            link = url +link
        if link[0:1] == "#":
            continue
        visited_links.add(link)
    return visited_links

visited_links = getlinks(url)

for link in visited_links:
    print(link)
