from bs4 import BeautifulSoup
from requests_html import HTMLSession

#{}
arbetsformedlingen = "https://arbetsformedlingen.se/platsbanken/annonser?l=3:kuMn_feU_hXx&page=1"

minsida = "https://arbetsformedlingen.se/platsbanken/annonser?l=3:kuMn_feU_hXx&page={}"
mina_yrken = ["lager", "truckförare", "data"]
max_antal_sidor = 2


session = HTMLSession()

r = session.get(arbetsformedlingen)

r.html.render(sleep=1, keep_page=True, scrolldown=3)

jobs = r.html.find("pb-feature-search-result-card")

for item in jobs:
    jobs = {
        "job": item.find("a")[0].text,
        "yrke": item.find("div")[5].text,
        "tid": item.find("div")[6].text,
        "link": item.absolute_links
    }
    print(jobs)

#This works
""" #For every webpage
for page in range(1,max_antal_sidor+1):
    url = arbetsformedlingen.format(page)
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text, 'lxml')
    print(url)
 """
