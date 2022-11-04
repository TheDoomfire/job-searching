from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import csv
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import re


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


def useSelenium(link):
    driver.get(link)
    time.sleep(1)
    linkButton = driver.find_element("link text", "Ansök här")
    anonsLink = linkButton.get_attribute("href") # Gets the url from the actually job website.
    getReferens(link)
    print(link)
    linkButton.click()


def getReferens(link):
    session = HTMLSession()
    r = session.get(link)
    r.html.render(sleep=1, keep_page=True, scrolldown=1) # Renders all javascript. scrolldown may be changed for large webpages
    annons = r.html.find("div", containing="Ange referens", first=True) # first=True means first time it finds it.
    referens = annons.find("strong", first=True)
    publicerad = r.html.find("h2", containing="Publicerad:", first=True)
    annonsLink = r.html.find("a", containing="Ansök här", first=True)

    print("Referens: ", referens.text)
    for i in annonsLink.absolute_links: # Stupied I have to do this. Only one link inside.
        annonsLink = i
    formatTime(publicerad.text)
    print(annonsLink)


def formatTime(the_text):
    the_text = re.split(":|,", the_text)
    the_text = the_text[1].strip()
    the_text = re.split(" ", the_text)
    day = the_text[0]
    year = the_text[2]
    if the_text[1] == "januari":
        month = 1
    elif the_text[1] == "februari":
        month = 2
    elif the_text[1] == "mars":
        month = 3
    elif the_text[1] == "april":
        month = 4
    elif the_text[1] == "maj":
        month = 5
    elif the_text[1] == "juni":
        month = 6
    elif the_text[1] == "juli":
        month = 7
    elif the_text[1] == "agusti":
        month = 8
    elif the_text[1] == "september":
        month = 9
    elif the_text[1] == "oktober":
        month = 10
    elif the_text[1] == "november":
        month = 11
    elif the_text[1] == "december":
        month = 12
    mydate = str(day) + "-" + str(month) + "-" + str(year) # Cant add string to integer so have to convert the integers.

    print(mydate)


with open("job-to-apply.csv") as f:
    reader = csv.reader(f)
    count = 0
    next(reader) # Skips the header row

    for row in reader:
        getReferens(row[4])
        if count > -1:
            break
        count += 1
