from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
# import csv
from bs4 import BeautifulSoup
# import requests
from requests_html import HTMLSession
# import re

# TODO
# Make beutifulsoup look for any referens in annons page.
# If it finds it, store it inside of a variable.
# Do same with date posted.
# Get all the links from annons arbetsförmedlingen.
# If 404, or any other kind of error. Stop it and go to next link.
# Inside of a link, try to find any fill out forms.
# If no fillout forms exist, look for "ansök här" link or button.
# Fill out forms.
# Upload CV.



PATH = r"D:\Documents\GitHub\job-searching\chromedriver.exe"
""" driver = webdriver.Chrome(PATH) # Opens the browser
driver.maximize_window() # Makes the browser fullscreen size. """



session = HTMLSession() # For requests_html
jobsToApplyFor = []


def useSelenium(link):
    driver.get(link)
    time.sleep(1)
    linkButton = driver.find_element("link text", "Ansök här")
    anonsLink = linkButton.get_attribute("href") # Gets the url from the actually job website.
    getReferens(link)
    print(link)
    linkButton.click()


def getReferens(link):
    r = session.get(link)
    r.html.render(sleep=1, keep_page=True, scrolldown=1) # Renders all javascript. scrolldown may be changed for large webpages
    annons = r.html.find("div", containing="Ange referens", first=True) # first=True means first time it finds it.
    annonsLink = r.html.find("a", containing="Ansök här", first=True)

    try:
        referens = annons.find("strong", first=True)
        referens = referens.text
    except:
        referens = None

    for i in annonsLink.absolute_links: # Stupid I have to do this. Only one link inside.
        annonsLink = i
    returnList = [annonsLink, referens]
    return returnList # TODO: return referens if not none/null

    theJob = {
    "link": annonsLink,
    "referens": referens.text # Maybe have to add a if statement if referens == None
    }

    print(theJob)


def webscrapeAnnons(link):
    r = session.get(link)
    r.html.render(sleep=1, keep_page=True, scrolldown=1) # Renders all javascript. scrolldown may be changed for large webpages

# Without referens
# print(getReferens("https://arbetsformedlingen.se/platsbanken/annonser/26773731"))

# With referens
# print(getReferens("https://arbetsformedlingen.se/platsbanken/annonser/26773558"))


""" with open("job-to-apply.csv") as f:
    reader = csv.reader(f)
    count = 0
    next(reader) # Skips the header row

    for row in reader:
        getReferens(row[4])
        if count > -1:
            break
        count += 1 """
