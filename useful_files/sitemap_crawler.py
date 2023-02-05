import requests
from bs4 import BeautifulSoup

# Get robots.txt file
r = requests.get("https://www.cnn.com/robots.txt")
robots_txt = r.text

# Extract sitemap from robots.txt
sitemap_index = robots_txt.find("Sitemap:")
sitemap_url = robots_txt[sitemap_index+8:].strip()

# Get the sitemap
sitemap = requests.get(sitemap_url).text

# Extract all URLs from the sitemap
soup = BeautifulSoup(sitemap, 'html.parser')
urls = [loc.text for loc in soup.find_all('loc')]

# Crawl each URL and store the HTML soup in a local file
for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Extract the file name from the URL
    file_name = url.split("/")[-1]

    # Write the HTML soup to the file
    with open(file_name, 'w') as f:
        f.write(str(soup))


