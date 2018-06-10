from bs4 import BeautifulSoup

import article
import requester

root_url = "http://www.voetbalzone.nl/"
source_url = "http://www.voetbalzone.nl/club.asp?uid=8"


def make_request():
    html = requester.get_html(source_url)
    return html


def get_articles():
    print("Getting articles from: " + source_url)
    html = make_request()
    soup = BeautifulSoup(html, "html.parser")
    lis = soup.find_all("ul", class_="reactiesList")

    arts = []

    for eles in lis:
        art = article.Article()
        art.title = eles.a.text
        art.source = "voetbalzone.nl"
        art.url = eles.a.get('href')
        art.full_url = root_url + art.url
        arts.append(art)
    return arts
