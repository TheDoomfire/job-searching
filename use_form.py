from requests_html import HTMLSession
from bs4 import BeautifulSoup
from my_variables import headers

# TODO:
# Find at all the Input text & Values & Types. Inside the form.
# Find all selects
# Find all radio buttons

# Find corresponding labels.
# In a select if id/name="selectgender, gender". Take value of option with the text "Män", if not exist take a random value?
# If label contains "Födelsedatum", go to the "for=" element.

the_url = "https://oak.varbi.com/se/apply/positionquick/640016/?where=1form"


def form_use(url):
    s = HTMLSession()
    r = s.get(url, headers=headers)
    r.html.render(sleep=1)
    soup = BeautifulSoup(r.text, 'html.parser')

    inputs = soup.find_all('inputs')
    forms = soup.find_all('form')
