from requests_html import HTMLSession
from bs4 import BeautifulSoup
import json
import time
from config_variables import btn_text_apply


the_url = "https://jobb.nercia.se/jobb/909/ansokningsformular"
test_url = "https://www.academicwork.se/jobs/a/lagermedarbetare-pa-heltid-till-elektroskandia/15096902?i=0"

problem_urls = ["https://career.netonnet.com/jobs/3031063-butiksmedarbetare-med-saljdriv?promotion=736376-arbetsformedlingen"
                "https://retail24.teamtailor.com/sv/jobs/3101468-demopersonal-retail24-orebro",
                "https://extra.orebro.se/jobb/ledigajobb/tjanst.4.7bb58d5d154d257e2bc24e06.html?rmpage=job&rmjob=16576&ref=https%3A%2F%2Farbetsformedlingen.se%2Fplatsbanken%2F",
                "https://www.experis.se/sv/jobb/6319d068-9350-4386-8693-1b149b5bd583/infoflex-systemvetare?aplitrak_email=Y2Fyb2RkLjgzNzYxLjMxMDFAbWFucG93ZXJncm91cG5vcmRpY3MuYXBsaXRyYWsuY29t&source=arbetsformedlingen&utm_source=AMS&utm_medium=Job-Board&utm_campaign=Broadbean&referer=aplitrak.com",
                "https://my.centric.eu/#/apply-job?JobId=287865F5-5643-EE11-8165-005056AD72DA&SourceChannel=Arbetsformedlingen.se(CNTRC0815858)",
                ]


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
# Some buttons are inputs!

# some form_url is still dynamic. Need to fix so it will apply jobs inside of this.

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Referer': 'https://arbetsformedlingen.se/', # Where we came from
    'DNT': '1' # Do Not Track
}

def modify_url(url):
    if url.startswith("//"):
        url = "https:" + url
    return url


# Maybe make it compare to .lower()
btn_text = ["ansök", "Ansök", "apply", "Apply", "sök tjänst", "Sök Tjänst", "Sök tjänst", "sök jobbet", "Sök jobbet", "Sök jobbet här", "SKICKA IN ANSÖKAN", "ANSÖK NU", "Ansök här"]


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


# with open('Albin Mustafa - CV.pdf', 'rb') as cv_file, open('Albin Mustafa - CV.pdf', 'rb') as letter_file:
with open('CV - Emma Åberg.pdf', 'rb') as cv_file, open('CV - Emma Åberg.pdf', 'rb') as letter_file:
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
    r.html.render(sleep=3, keep_page=True, scrolldown=5)
    soup = BeautifulSoup(r.text, 'html.parser')

    forms = soup.find_all('form')
    buttons = soup.find_all('button')
    links = soup.find_all('a')
    iframes = soup.find_all('iframe') # Since some webpages have everything inside of a iframe. Weird.
    # Dosent work if it isnt any frames?
    form_url = None

    if forms:
        for form in forms:
            print("Found a form.")
            inputs = form.find_all('input')
            if len(inputs) >= 4: # Because a job searching for is typically at least 4 forms. Maybe look for 2 upload forms.
                inputs = form.find_all('input', {'type': 'file'})
                if len(inputs) >= 2:
                    print("Form with minimum of 2 file input fields found!")
                    form_url = url
                    # action_url = form['action']
                    input_fields = form.find_all('input')
                    # JUST FOR TESTING
                    button = soup.find('button', string='Ansök') # TODO: Also add "ANSÖK"
                    if button:
                        parent_form = button.find_parent('form')
                        if parent_form:
                            inputs = parent_form.find_all('input')
                            payload = {input['name']: input.get('value', '') for input in inputs}
                            print("----THE PAYLOAD----")
                            print(payload) # Finds our all the data that needs to be sent.
                            print("----END PAYLOAD----")


                            # Prepare the payload data
                            # payload = {field['name']: field.get('value', '') for field in input_fields}
                            # Submit the form
                            #response = s.post(url, data=form_text_data)
                            #if response.status_code == 200:
                            #    print("Form submitted successfully")
                            #else:
                            #    print("Failed to submit form")
                    return form_url
            for value in btn_text:
                submit_input = soup.find('input', {'type': 'submit', 'value': value})
                if submit_input:
                    print("found a submit with value")
                    form_url = url
                    return form_url
    elif buttons:
        for button in buttons:
            if button.text.strip() in btn_text: # Maybe make it compare to .lower()
                print("Button with text '{}' found!".format(button.text.strip()))
                print("BUTTON")
                form_url = url
                return form_url
    if links:
        for link in links:
            link_with_text = link.text.strip()
            #print(link_with_text)
            if link_with_text in btn_text: # Maybe make it compare to .lower()
                print(link_with_text)
                #print("LINK: ", link)
                link_href = link.get('href')
                if link_href:
                    print("Link with text '{}' found!".format(link_with_text))
                    print(link)
                    print("Link Href:", link_href)
                    # time.sleep(5) # Need to have a sleep otherwise may get problems with headers.
                    # form_search(link_href) # May need to rerun it if I want to continue serarch for forms.
                    if link_href.startswith("#"): # Some links are just innerlinks to the same page and they start with #
                        form_url = url + link_href
                    else:
                        form_url = link_href
                    return form_url
    if iframes:
        iframe_url = modify_url(iframes[0]['src']) # Incase it starts with // will change to https://
        print("Iframes :(")
        print(iframe_url)
        for frames in iframes:
            print(frames)
    print("No Form: ", url)

    #print(soup)


# print(form_search(test_url))

# {'firstName': '', 'surName': '', 'email': '', 'linkedInUrl': '', '1019': '', '2150': '', '2151': '', '2160': '', '2212': '', '2289': '', 'cv': '', 'other-document': '', 'consent': ''}



# Looking for downloadable input fields.
# Past in forms
"""     inputs = form.find_all('input', {'type': 'file'})
    if len(inputs) >= 2:
        print("Form with minimum of 2 file input fields found!")
        break """
