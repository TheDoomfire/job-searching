from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests
import pandas as pd


mina_yrken = ["lager", "truckförare", "lagerarbetare", "data", "it-tekniker", "truck"]
skit_arbetsgivare = ["tranpenad", "dhl"]
blocked_title_text = ["åsbro"]
max_antal_sidor = 2


""" def page(max_antal_sidor):
    for page in range(1,max_antal_sidor+1):
       url = arbetsformedlingen.format(page)
       html_text = requests.get(url)
       soup = BeautifulSoup(html_text, 'lxml')
    return(url) """

def extract(pagenumber):
    website = "https://arbetsformedlingen.se/platsbanken/annonser?l=3:kuMn_feU_hXx&page={}"
    session = HTMLSession()
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
    url = website.format(pagenumber)
    r = session.get(url)
    r.html.render(sleep=1, keep_page=True, scrolldown=1)
    return(r)


"""     for page in range(1,max_antal_sidor+1):
       url = arbetsformedlingen.format(page)
       html_text = requests.get(url)
       soup = BeautifulSoup(html_text, 'lxml') """


def transform(r):
    job_card = r.html.find("pb-feature-search-result-card")
    for item in job_card:
      if any(yrke in item.find("div")[5].text.lower() for yrke in mina_yrken) and not any(arbetsgivare in item.find("strong")[0].text.lower() for arbetsgivare in skit_arbetsgivare):
        jobb = item.find("a")[0].text
        y = item.find("div")[5].text
        company = item.find("strong")[0].text
        tid = item.find("div")[6].text
        link = item.absolute_links
        job = {
            "jobb": jobb,
            "yrke": y,
            "company": company,
            "tid": tid,
            "link": link,
            "applied": False
        }
        joblist.append(job)
    return


joblist = []

# Över 25 laggar. error at 43 pyppeteer.errors.TimeoutError: Navigation Timeout Exceeded: 8000 ms exceeded..
for i in range(0, 5):
    print(f"Getting page, {i}")
    c = extract(i)
    transform(c)


df = pd.DataFrame(joblist)
df.to_csv("jobs.csv")


""" def search_jobb():
    for item in jobs:
        if any(yrke in item.find("a")[0].text.lower() for yrke in mina_yrken):
           jobb = item.find("a")[0].text
           print(jobb) """



"""     for page in range(1,max_antal_sidor+1):
       url = arbetsformedlingen.format(page)
       html_text = requests.get(url)
       soup = BeautifulSoup(html_text, 'lxml') """

""" for item in jobs:
    #if any(yrken in mina_yrken for yrken in item):
       jobs = {
        "job": item.find("a")[0].text,
        "yrke": item.find("div")[5].text,
        "tid": item.find("div")[6].text,
        "link": item.absolute_links
        } """