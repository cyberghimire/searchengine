from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlparse
from bs4 import BeautifulSoup


def get_page(url):

    response = urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))
    soup = BeautifulSoup(response, 'html.parser', from_encoding=response.info().get_param('charset'))
    
    return soup

robots = get_page("https://www.facebook.com/robots.txt")
print(robots)

def get_sitemaps(robots):
    data = []
    lines = str(robots).lower().splitlines()

    for line in lines:
        if line.startswith('sitemap:'):
            split = line.split(':', maxsplit = 1)
            data.append(split[1].strip())

    return data

def get_allowed(robots):
    allowed = set()
    lines = str(robots).lower().splitlines()

    for line in lines:
        if line.startswith('allow:'):
            split = line.split(':', maxsplit = 1)
            allowed.add(split[1])
    return allowed

sitemaps = get_sitemaps(robots)
print(sitemaps)

allowed = get_allowed(robots)
print(allowed)

