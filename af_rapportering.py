import csv
import time
import datetime
from playwright.sync_api import Playwright, sync_playwright, expect


the_file = "applied_jobs.csv"
todayDate = datetime.datetime.now().date() # Todays date
month = todayDate.month
first_day_of_previous_month = todayDate.replace(day=1) - datetime.timedelta(days=todayDate.day)
#first_day_of_current_month = todayDate.replace(day=1)

#TODO:
# Read from a .csv file.
# Use playwright to submit


def rapportering() -> None: # Can remove None when it returns something.
    url_af = "https://idp.ciceron.cloud/authn-wpki.dialog?device=other&idp=wpki2&id=_5f17830a888b297b777b360b03955bfe68f5e12c&client=bankid&system=arbetsformedlingen_bankid_mobile&sessionid=8f5e81b615704e7f05bc21629960e6d9cd7ba15809"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url_af)
        # Login
        page.get_by_placeholder("ÅÅÅÅMMDDNNNN").click()
        page.get_by_placeholder("ÅÅÅÅMMDDNNNN").fill("199409096030")
        page.get_by_role("button", name="Logga in").click()
        page.get_by_role("button", name="Jag godkänner alla kakor").click()
        page.get_by_role("link", name="Aktivitetsrapportera").click()
        page.get_by_role("link", name="Rapportera dina aktiviteter").first.click()
        page.get_by_role("button", name="Lägg till aktiviteter").click()

        with open(the_file, 'r') as csv_file:
            # Create a CSV reader object
            csv_reader = csv.reader(csv_file)

            # next(csv_reader)  # Skip the first row
            
            # Iterate through the rows of the CSV file
            for row in csv_reader:
                # Process each row (each row is a list)
                occupation = row[1]
                organization = row[2]
                title = row[3]
                date_posted = row[7]
                date_obj = datetime.datetime.strptime(date_posted, "%Y-%m-%d").date()
                the_date = date_posted
                if date_obj.month < month:
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
                page.get_by_label("Vilket datum sökte du jobbet?").fill(the_date)
                page.get_by_role("button", name="Spara").click()


            browser.close()

            # TODO: Add 


        time.sleep(10)

def open_csv():
    # Open the CSV file in read mode
    with open(the_file, 'r') as csv_file:
        # Create a CSV reader object
        csv_reader = csv.reader(csv_file)

        # next(csv_reader)  # Skip the first row
        
        # Iterate through the rows of the CSV file
        for row in csv_reader:
            # Process each row (each row is a list)
            occupation = row[1]
            organization = row[2]
            title = row[3]
            date_posted = row[7]
        # TODO: Add 



rapportering()