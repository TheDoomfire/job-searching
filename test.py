from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests
import pandas as pd


def extract(website):
    session = HTMLSession()
    r = session.get(website)
    r.html.render(sleep=1, keep_page=True, scrolldown=1)
    return(r)


min_referens = ""
ansok_har = ""


def get_info(r):

    hitta_referens = r.html.find('div', containing='Ange referens')
    for item in hitta_referens:
        referens = item.find("strong")[0].text
        min_referens = referens
        print(referens)
        break

    apply_here = r.html.find('a', containing='Ansök här')
    for item in apply_here:
        link = item.absolute_links
        ansok_har = link
        print(link)




get_info(extract("https://arbetsformedlingen.se/platsbanken/annonser/26273250"))
print(min_referens)

