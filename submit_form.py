from requests_html import HTMLSession
from bs4 import BeautifulSoup
import json
import time
# from playwright.sync_api import sync_playwright
from playwright.sync_api import Playwright, sync_playwright, expect
from config_variables import header_af, payload_data


# TODO:
# Copy from look_for_forms
# use it with playwright instead.
# if form found, type everything inside of it.
# detect if sending form was successful


# Maybe make it compare to .lower()
btn_text = ["ansök", "Ansök", "apply", "Apply", "sök tjänst", "Sök Tjänst", "Sök tjänst", "sök jobbet", "Sök jobbet", "Sök jobbet här"]
btn_cookie_accept = ["Jag förstår", "Accept all", "GODKÄNN ALLA KAKOR"]
label_email_texts = ["Email*", "Epost*", "E-post*"]
submit_input = None
test_url = "https://www.pallkonsulten.se/jobb/nu-soker-vi-erfaren-truckforare/"
# https://apply.recman.no/job_post.php?id=341738&path=ams&sub_id=462
# https://jobs.aditrologistics.com/jobb/3196/ansokningsformular/
# https://emp.jobylon.com/applications/jobs/164268/create/?utm_source=ams&utm_medium=promotionserializer

def modify_url(url):
    if url.startswith("//"):
        url = "https:" + url
    return url


def form_search(url):
    s = HTMLSession()
    r = s.get(url, headers=header_af)
    r.html.render(sleep=2, keep_page=True, scrolldown=1)
    soup = BeautifulSoup(r.text, 'html.parser')

    forms = soup.find_all('form')
    buttons = soup.find_all('button')
    links = soup.find_all('a')
    iframes = soup.find_all('iframe') # Since some webpages have everything inside of a iframe. Weird.
    # Dosent work if it isnt any frames?
    print(url + "form") # Maybe stupid to have form.
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
            if link.text.strip() in btn_text: # Maybe make it compare to .lower()
                print("Link with text '{}' found!".format(link.text.strip()))
                link_href = link.get('href')
                print("Link Href:", link_href)
                time.sleep(5) # Need to have a sleep otherwise may get problems with headers.
                form_search(link_href)
                form_url = url
                return form_url
    if iframes:
        iframe_url = modify_url(iframes[0]['src']) # Incase it starts with // will change to https://
        print("Iframes :(")
        print(iframe_url)
        for frames in iframes:
            print(frames)

# async
""" def submit_form(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto(url)
        html = page.content() # await
        soup = BeautifulSoup(html, 'html.parser')
        forms = soup.find_all('form')
        buttons = soup.find_all('button')
        links = soup.find_all('a')
        iframes = soup.find_all('iframe') # Since some webpages have everything inside of a iframe. Weird.

        if forms: # TODO: Sometimes forms are found but not visible in the browser.
            for form in forms:
                print("Found a form.")
                inputs = form.find_all('input')
                if len(inputs) >= 4: # Because a job searching for is typically at least 4 forms. Maybe look for 2 upload forms.
                    inputs = form.find_all('input', {'type': 'file'})
                    if len(inputs) >= 2:
                        print("Form with minimum of 2 file input fields found!")
                        print("---------- THE FORM ----------")
                        print(form)
                        print("---------- THE INPUTS ----------")
                        print(inputs)

                for value in btn_text:
                    submit_input = soup.find('input', {'type': 'submit', 'value': value})
                    if submit_input:
                        print("found a submit with value")
                        # Maybe need to click it. """


""" def submit_form(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto(url)
        html = page.content() # await
        page.click('text=Accept')
        # soup = BeautifulSoup(html, 'html.parser')
        # btn_cookie_accept
        cookie_button = page.locator("button:text({})".format(btn_cookie_accept))
        cookie_button.click()
        page.waitForTimeout(5000) """



"""         for text in btn_cookie_accept:
            cookie_button = page.get_by_role("button", name=text)
            if cookie_button:
                cookie_button.click()
                break
 """


def submit_form(url) -> None: # Can remove None when it returns something.
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)

        for text in btn_cookie_accept:
            try:
                cookie_button = page.get_by_role("button", name=text)
                if cookie_button:
                    cookie_button.click()
                    break  # Exit the loop once a button is clicked
            except Exception as e:
                print(f"An error occurred: {str(e)}")
        #page.get_by_role("button", name="Accept all").click() # Cookie
        #page.wait_for_load_state("networkidle") # For cookie?
        #time.sleep(2)
        #page.mouse.wheel(0, 100)
        #time.sleep(4)
        # TODO: Some inputs dosent have a label with for...
        page.wait_for_selector('label:has-text("Förnamn*")')
        page.get_by_label("Förnamn*").scroll_into_view_if_needed()
        page.get_by_label("Förnamn*").click()
        page.get_by_label("Förnamn*").fill(payload_data["name"])
        page.get_by_label("Efternamn*").scroll_into_view_if_needed()
        page.get_by_label("Efternamn*").click()
        page.get_by_label("Efternamn*").fill(payload_data["lastname"])
        #Epost or Email label_email_texts
        for text in label_email_texts:
            try:
                email_label = page.get_by_label(text)
                if email_label:
                    page.get_by_label(text).scroll_into_view_if_needed()
                    page.get_by_label(text).click()
                    page.get_by_label(text).fill(payload_data["email"])
                    break
            except Exception as e:
                print(f"An error occurred: {str(e)}")

        #page.get_by_label("Epost*").scroll_into_view_if_needed()
        #page.get_by_label("Epost*").click()
        #page.get_by_label("Epost*").fill(payload_data["email"])
        page.get_by_role("combobox", name="Unknown").scroll_into_view_if_needed()
        page.get_by_role("combobox", name="Unknown").click()
        page.get_by_role("option", name="Sweden (Sverige)+46").scroll_into_view_if_needed()
        page.get_by_role("option", name="Sweden (Sverige)+46").click()
        # or name="your-phone". Go for label instead?
        # page.get_by_label("Telefon*").scroll_into_view_if_needed() #PROBLEM Telefon Telefonnummer
        # page.get_by_label("Telefon*").click()
        # page.get_by_label("Telefon*").fill(payload_data["phone"])
        page.locator("input[type=\"tel\"]").scroll_into_view_if_needed()
        page.locator("input[type=\"tel\"]").click()
        page.locator("input[type=\"tel\"]").fill(payload_data["phone"])
        # page.get_by_label("Telefonnummer*").scroll_into_view_if_needed()
        # page.get_by_label("Telefonnummer*").click()
        # page.get_by_label("Telefonnummer*").fill(payload_data["phone"])
        # page.get_by_role("option", name="Sweden (Sverige)+46").click() # Donno how to find it...
        # page.click('option:has-text-matching("/\+46/")')

        # page.get_by_label("CV").click()
        # page.get_by_label("CV").set_input_files(payload_data["cv"])

        page.get_by_label(payload_data["sex"]).scroll_into_view_if_needed()
        page.get_by_label(payload_data["sex"]).check()

        # samtycker, bekräftar, godkänner
        page.get_by_label("Jag bekräftar att jag har läst följande information om behandling av personuppgifter*").check() # Need to check all

        time.sleep(10)

        # page.get_by_role("button", name="Skicka").click()
        # TODO: Add a check to see if its bent sent?
        # ---------------------
        context.close()
        browser.close()


submit_form(test_url)
print("DONE!")