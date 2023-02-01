from requests_html import HTMLSession
from bs4 import BeautifulSoup





""" buttons = soup.find_all('button')

for button in buttons:
    if button.text.strip() in ["Hello", "hello", "Hey", "hej"]:
        print("Button with text '{}' found!".format(button.text.strip()))
        break
else:
    print("No button with text 'Hello', 'hello', 'Hey', or 'hej' found.")
 """


# TODO:
# Look for form tag
# If not found:
# look for button, or a tag with the text "ansök"
# take that link and run the function on it. If its not the same as the link already provided.

hej = 0
def form_search(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)
    if hej == 1:
        print("Its 1")
    elif hej == 2:
        print("Its 2")