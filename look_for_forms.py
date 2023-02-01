from requests_html import HTMLSession
from bs4 import BeautifulSoup
import json


the_url = "https://apply.recman.no/job_post.php?id=314240&path=ams&sub_id=462"


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
# <form

# Maybe make it compare to .lower()
btn_text = ["ansök", "Ansök", "apply", "Apply", "sök tjänst", "Sök Tjänst", "Sök tjänst"]


with open('form_data.json', 'r') as f:
    form_data = json.load(f)

# The payload
form_text_data = {
    "name": form_data["name"],
    "namn": form_data["name"],
    "first_name": form_data["name"],
    "lastname": form_data["last_name"],
    "last_name": form_data["last_name"],
    "email": form_data["email"],
    "phone-prefix": form_data["phone_prefix"],
    "phone": form_data["phone"],
    "phone_number": form_data["phone"],
    "address": form_data["address"]
}


with open('Albin Mustafa - CV.pdf', 'rb') as cv_file, open('Albin Mustafa - CV.pdf', 'rb') as letter_file:
    form_files = {
        'cv': cv_file,
        'personal_letter': letter_file,
        'file[]': letter_file
    }


hej = 0
def form_search(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)
    soup = BeautifulSoup(r.text, 'html.parser')

    forms = soup.find_all('form')
    buttons = soup.find_all('button')
    links = soup.find_all('link')

    if forms:
        for form in forms:
            inputs = form.find_all('input')
            if len(inputs) >= 4: # Because a job searching for is typically at least 4 forms. Maybe look for 2 upload forms.
                inputs = form.find_all('input', {'type': 'file'})
                if len(inputs) >= 2:
                    print("Form with minimum of 2 file input fields found!")
                    action_url = form['action']
                    input_fields = form.find_all('input')
                    # Prepare the payload data
                    # payload = {field['name']: field.get('value', '') for field in input_fields}
                    # Submit the form
                    # response = s.post(action_url, data=payload)
                    break 
    elif buttons:
        for button in buttons:
            if button.text.strip() in btn_text: # Maybe make it compare to .lower()
                print("Button with text '{}' found!".format(button.text.strip()))
                break


form_search(the_url)



# Looking for downloadable input fields.
# Past in forms
"""     inputs = form.find_all('input', {'type': 'file'})
    if len(inputs) >= 2:
        print("Form with minimum of 2 file input fields found!")
        break """