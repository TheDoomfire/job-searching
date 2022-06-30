from bs4 import BeautifulSoup
from requests_html import HTMLSession

arbetsformedlingen = "https://arbetsformedlingen.se/platsbanken/annonser?l=3:kuMn_feU_hXx&page=1"

minsida = "https://arbetsformedlingen.se/platsbanken/annonser?l=3:kuMn_feU_hXx&page={}"
jobs = ["lager", "truckförare"]
max_antal_sidor = 2


session = HTMLSession()

r = session.get(arbetsformedlingen)

r.html.render(sleep=1, keep_page=True, scrolldown=3)

jobs = r.html.find("pb-feature-search-result-card")

for item in jobs:
    jobs = {
        "job": item.find("a")[0].text,
        "job_titel": item.find("div")[5].text,
        "time": item.find("div")[6].text,
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



""" html_text = requests.get(arbetsformedlingen)
#soup = BeautifulSoup(html_text, "lxml")
doc = BeautifulSoup(html_text.text, "html.parser")

cards = doc.find_all("h3")

print(cards) """