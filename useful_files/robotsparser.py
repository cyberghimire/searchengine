import requests

# Specify the URL of the robots.txt file
robots_url = "http://www.bbc.com/robots.txt"

# Send a request to the robots.txt URL
response = requests.get(robots_url)

# Extract the lines of the robots.txt file
lines = response.text.split("\n")

# Find all the lines that start with "Sitemap:"
sitemaps = [line for line in lines if line.startswith("Sitemap:")]

# Print and store the sitemaps
with open("sitemaps.txt", "w") as f:
    for sitemap in sitemaps:
        print(sitemap)
        f.write(sitemap + "\n")



with open("sitemaps.txt", "r") as f:
    sitemaps = f.readlines()

# Extract the links from the sitemaps
links = [sitemap.strip().replace("Sitemap: ", "") for sitemap in sitemaps]

# Print the links
for link in links:
    print(link)