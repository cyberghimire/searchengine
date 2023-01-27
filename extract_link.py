import requests
from bs4 import BeautifulSoup

# Set the URL of the webpage that you want to crawl
url = "https://www.cnn.com"

# Download the HTML of the webpage
response = requests.get(url)
html = response.text

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find all links in the HTML
links = soup.find_all("a")

# Print the links
for link in links:
    print(link.get("href"))