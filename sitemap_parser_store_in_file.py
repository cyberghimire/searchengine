import requests
from bs4 import BeautifulSoup

# Specify the URL of the sitemap
sitemap_url = "http://www.cnn.com.np/sitemap.xml"

# Send a request to the sitemap URL
response = requests.get(sitemap_url)

# Parse the XML content of the sitemap
soup = BeautifulSoup(response.content, "xml")

# Find all the URLs in the sitemap
urls = [loc.text for loc in soup.find_all("loc")]

# Crawl and store the websites
for url in urls:
    # Send a request to the website URL
    response = requests.get(url)
    # Extract the website content
    website_content = response.text
    # Write the website content to a text file
    with open(url.replace("/", "_") + ".txt", "w") as f:
        f.write(website_content)
