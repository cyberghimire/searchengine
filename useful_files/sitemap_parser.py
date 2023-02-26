import pandas as pd
import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import xmltodict
import requests

def get_sitemap(url):

    response = urllib.request.urlopen(url)
    xml = BeautifulSoup(response, features="xml",
                         from_encoding=response.info().get_param('charset'))

    return xml

url = "https://www.cnn.com/sitemap.xml"
xml = get_sitemap(url)

def get_sitemap_type(xml):

    sitemapindex = xml.find_all('sitemapindex')
    sitemap = xml.find_all('urlset')

    if sitemapindex:
        return 'sitemapindex'
    elif sitemap:
        return 'urlset'
    else:
        return

sitemap_type = get_sitemap_type(xml)
print(f"sitemap type is {sitemap_type}" )


def get_child_sitemaps(xml):

    sitemaps = xml.find_all("sitemap")

    output = []

    for sitemap in sitemaps:
        output.append(sitemap.findNext("loc").text)
    return output

child_sitemaps = get_child_sitemaps(xml)
print (f"child sitemap are {child_sitemaps}")

