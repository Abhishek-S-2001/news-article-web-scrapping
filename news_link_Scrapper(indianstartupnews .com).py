# Scrapping News Article links from the website
# Links Scrapped from indianstartupnews.com


from asyncio.windows_events import NULL
import requests
from bs4 import BeautifulSoup
from regex import regex as re

url = "https://indianstartupnews.com/"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')

# Get all the anchor tags from the page
anchors = soup.find_all('a')
all_links = []
article_link = []
urls = []
# Get all the links on the page:
for link in anchors:
    if(link.get('href') != '#'): 
        linkText = "" +link.get('href')
        all_links.append(linkText)
        # print(linkText)
# print(len(all_links))
# print(all_links)

# finding news Link
for i in range(len(all_links)):
    line = all_links[i]
    line = re.findall('https?://indianstartupnews.com/news/(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)           # Used regex
    if line!=NULL:
        urls.append(line)

# Removing Null Indexes
urls = list(filter(None, urls))

# Removing Duplicate Links
res = []
for i in urls:
    if i not in res:
        res.append(i)
print(len(res))

# Printing Links
for i in res:
    print(i)
