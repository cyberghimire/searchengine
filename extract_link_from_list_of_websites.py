import requests
from bs4 import BeautifulSoup

def extract_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            links.append(href)
    return links

websites = ['localhost:5000/a', 'localhost:5000/b', 'localhost:5000/c', 'localhost:5000/d', 'localhost:5000/e']
all_links = {}
for website in websites:
    url = 'http://' + website
    links = extract_links(url)
    all_links[website] = links

print(all_links)
