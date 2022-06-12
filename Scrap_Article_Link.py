# # Scrapping News Article links from the website

from __future__ import print_function
from requests import session
from requests_html import HTMLSession

# Using requests and Html Session

session = HTMLSession()

def find_article(url, htag):
    print(url)

    r = session.get(url)

    r.html.render(sleep=1, scrolldown=5, timeout=50)

    articles = r.html.find('article')
    newslist = []

    for item in articles:
        try:
            newsitem = item.find(htag, first=True)
            title = newsitem.text                                   # getting title 
            link = newsitem.absolute_links                          # getting Article Link
            newsarticle = {
                'title': title,
                'link': link 
            }
            newslist.append(newsarticle)
        except:
            pass

    print(len(newslist))
    for i in newslist:
        print(i)
        print("\n")


find_article('https://techcrunch.com/', 'h2')                     # Article Links Scrapped
find_article('https://news.crunchbase.com/', 'h2')                # Article Links Scrapped
find_article('https://entrackr.com/', 'h3')                       # Article Links Scrapped

# # find_article('https://m.economictimes.com/tech/startups', 'h4')
# # find_article('https://www.livemint.com/companies/start-ups','h2')
# # find_article('https://www.entrepreneur.com/in','h3')
# # find_article('https://indianstartupnews.com/','h3')


# # Article Links stored in Lists in dictionary format with key and pair # #