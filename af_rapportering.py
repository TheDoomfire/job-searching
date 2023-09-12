import csv
import time
import datetime
from playwright.sync_api import Playwright, sync_playwright, expect


the_file = "jobs-i-will-apply-for.csv"
todayDate = datetime.datetime.now().date() # Todays date
month = todayDate.month
first_day_of_previous_month = todayDate.replace(day=1) - datetime.timedelta(days=todayDate.day)
#first_day_of_current_month = todayDate.replace(day=1)

#TODO:
# Read from a .csv file.
# Use playwright to submit


def rapportering() -> None: # Can remove None when it returns something.
    url_af = "https://arbetsformedlingen.se/systemsidor/inloggning"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url_af)
        # Cookie
        page.get_by_role("button", name="Jag godkänner alla kakor").click()

        page.get_by_role("link", name="Logga in som arbetssökande med mobilt BankID").click()

        # Login
        page.get_by_placeholder("ÅÅÅÅMMDDNNNN").click()
        page.get_by_placeholder("ÅÅÅÅMMDDNNNN").fill("199409096030")
        page.get_by_role("button", name="Logga in").click()
        page.get_by_role("link", name="Aktivitetsrapportera").click()
        # page.get_by_role("link", name="Rapportera dina aktiviteter").click() #page.get_by_role("link", name="Rapportera dina aktiviteter").first.click()
        page.get_by_role("button", name="Lägg till aktiviteter").scroll_into_view_if_needed()
        page.get_by_role("button", name="Lägg till aktiviteter").click()

        with open(the_file, 'r', encoding='utf-8') as csv_file:
            # Create a CSV reader object
            csv_reader = csv.reader(csv_file)

            next(csv_reader)  # Skip the first row
            
            # Iterate through the rows of the CSV file
            for row in csv_reader:
                # Process each row (each row is a list)
                occupation = row[1]
                organization = row[2]
                date_posted = row[8]
                #date_obj = datetime.datetime.strptime(date_posted, "%Y-%m-%d").date()
                the_date = date_posted
                date_parts = date_posted.split("-")
                date_month = int(date_parts[1])
                if date_month < month - 1: # ERROR: String and int?
                    the_date = first_day_of_previous_month
                page.get_by_label("Genom annons").scroll_into_view_if_needed()
                page.get_by_label("Genom annons").check()
                page.get_by_placeholder("Arbetsgivare").scroll_into_view_if_needed()
                page.get_by_placeholder("Arbetsgivare").click()
                page.get_by_placeholder("Arbetsgivare").fill(organization)
                page.get_by_placeholder("Typ av jobb").scroll_into_view_if_needed()
                page.get_by_placeholder("Typ av jobb").click()
                page.get_by_placeholder("Typ av jobb").fill(occupation)
                page.get_by_placeholder("Ort").scroll_into_view_if_needed()
                page.get_by_placeholder("Ort").click()
                page.get_by_placeholder("Ort").fill("Örebro")
                page.get_by_label("Vilket datum sökte du jobbet?").scroll_into_view_if_needed()
                page.get_by_label("Vilket datum sökte du jobbet?").click()
                page.get_by_label("Vilket datum sökte du jobbet?").fill(the_date) # ERROR: Object of type date is not JSON serializable
                page.get_by_role("button", name="Spara").click()


        # Button with the text: Till Min aktivitetsrapport
        # Button with the text: Kontrollera och skicka in
        # Button with the text:  Skicka in rapport 
        browser.close()

            # TODO: Add 


        time.sleep(10)

def open_csv():
    # Open the CSV file in read mode
    with open(the_file, 'r', encoding='utf-8') as csv_file:
        # Create a CSV reader object
        csv_reader = csv.reader(csv_file)

        next(csv_reader)  # Skip the first row
        
        # Iterate through the rows of the CSV file
        for row in csv_reader:
            # Process each row (each row is a list)
            occupation = row[1]
            organization = row[2]
            title = row[3]
            date_posted = row[8]
            #date_obj = datetime.datetime.strptime(date_posted, "%y-%m-%d").date()
            date_parts = date_posted.split("-")
            print("occupation: ", occupation)
            print("organization: ", organization)
            print("date_posted: ", date_posted)
            date_month = int(date_parts[1])
            #print(date_obj)
            the_date = date_posted
            #if date_month < month:
             #   the_date = first_day_of_previous_month 
            if date_month < month - 1: # ERROR: String and int?
                the_date = first_day_of_previous_month

            #print(date_posted)
            #print(the_date)
            #print(date_obj)
            print(the_date)
            print("Month: ", date_month)
            if isinstance(date_month, int):
                print("Integer")
            else:
                print("String?")
        print("Today: ", todayDate)
        print("Month: ", month)



rapportering()
open_csv()