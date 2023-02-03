from requests_html import HTMLSession
from bs4 import BeautifulSoup
import json
import time


the_url = "https://trv.heroma.se/prod/trvpp01/externwebbv2/LedigaJobb/EW2PageJobPostingAdvert.aspx?jobpostingid=7277691825931409813"


# https://www.lernia.se/jobb/lager-och-logistik/orebro-sommarjobba-som-materialhanterare-pa-epiroc-230735/
# https://performiq.se/lediga-jobb/6998/
# https://trv.heroma.se/prod/trvpp01/externwebbv2/LedigaJobb/EW2PageJobPostingAdvert.aspx?jobpostingid=7277691825931409813



# Söktes detta jobb???
# https://jobb.performiq.se/jobb/6998/ansok/

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
# look for button, or a tag with the text "ansök" + more
# take that link and run the function on it. If its not the same as the link already provided.
# If not found anything, save the link somewhere. So I can later look myself for it.
# If found and sent, change its applied for somewhere.
# Move to next url
# <form


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Referer': 'https://www.google.com', # Where we came from
    'DNT': '1' # Do Not Track
}


# Maybe make it compare to .lower()
btn_text = ["ansök", "Ansök", "apply", "Apply", "sök tjänst", "Sök Tjänst", "Sök tjänst", "sök jobbet", "Sök jobbet", "Sök jobbet här"]


with open('form_data.json', 'r') as f:
    form_data = json.load(f)

# The payload
form_text_data = {
    "name": form_data["name"],
    "namn": form_data["name"],
    "first_name": form_data["name"],
    "firstName": form_data["name"],
    "lastname": form_data["last_name"],
    "last_name": form_data["last_name"],
    "surName": form_data["last_name"],
    "email": form_data["email"],
    "phone-prefix": form_data["phone_prefix"],
    "phone": form_data["phone"],
    "mobilePhone": form_data["phone"],
    "phone_number": form_data["phone"],
    "address": form_data["address"]
}


with open('Albin Mustafa - CV.pdf', 'rb') as cv_file, open('Albin Mustafa - CV.pdf', 'rb') as letter_file:
    form_files = {
        'cv': cv_file,
        'personal_letter': letter_file,
        'file[]': letter_file,
        'other-document': letter_file
    }


hej = 0
submit_input = None
def form_search(url):
    s = HTMLSession()
    r = s.get(url, headers=headers)
    r.html.render(sleep=1)
    soup = BeautifulSoup(r.text, 'html.parser')

    forms = soup.find_all('form')
    buttons = soup.find_all('button')
    links = soup.find_all('a')
    iframes = soup.find_all('iframe') # Since some webpages have everything inside of a iframe. Weird.
    # Dosent work if it isnt any frames?
    print(url + "form")

    if forms:
        for form in forms:
            inputs = form.find_all('input')
            if len(inputs) >= 4: # Because a job searching for is typically at least 4 forms. Maybe look for 2 upload forms.
                inputs = form.find_all('input', {'type': 'file'})
                if len(inputs) >= 2:
                    print("Form with minimum of 2 file input fields found!")
                    # action_url = form['action']
                    input_fields = form.find_all('input')
                    # JUST FOR TESTING
                    button = soup.find('button', string='Ansök')
                    if button:
                        parent_form = button.find_parent('form')
                        if parent_form:
                            inputs = parent_form.find_all('input')
                            payload = {input['name']: input.get('value', '') for input in inputs}
                            print(payload) # Finds our all the data that needs to be sent.


                            # Prepare the payload data
                            # payload = {field['name']: field.get('value', '') for field in input_fields}
                            # Submit the form
                            response = s.post(url, data=form_text_data)
                            if response.status_code == 200:
                                print("Form submitted successfully")
                            else:
                                print("Failed to submit form")
                    break
            for value in btn_text:
                submit_input = soup.find('input', {'type': 'submit', 'value': value})
                if submit_input:
                    print("found a submit with value")
                    break
    elif buttons:
        for button in buttons:
            if button.text.strip() in btn_text: # Maybe make it compare to .lower()
                print("Button with text '{}' found!".format(button.text.strip()))
                print("BUTTON")
                break
    if links:
        for link in links:
            if link.text.strip() in btn_text: # Maybe make it compare to .lower()
                print("Link with text '{}' found!".format(link.text.strip()))
                link_href = link.get('href')
                print("Link Href:", link_href)
                time.sleep(5) # Need to have a sleep otherwise may get problems with headers.
                form_search(link_href)
                break
    if iframes:
        iframe_url = iframes[0]['src']
        print("Iframes :(")
        for frames in iframes:
            print(frames)


form_search(the_url)

# {'firstName': '', 'surName': '', 'email': '', 'linkedInUrl': '', '1019': '', '2150': '', '2151': '', '2160': '', '2212': '', '2289': '', 'cv': '', 'other-document': '', 'consent': ''}



# Looking for downloadable input fields.
# Past in forms
"""     inputs = form.find_all('input', {'type': 'file'})
    if len(inputs) >= 2:
        print("Form with minimum of 2 file input fields found!")
        break """