import datetime
from af_rapportering import rapportering
from job_gui import process_rows
# import download_jobtechdev # My file
from download_jobtechdev import zipDownloader
from open_all_links import open_all_urls
from use_jobtechdev import readTheJson
import os
# import use_jobtechdev # My file

# Run only this file.

# BIG TODO
# Make playwright auto applying the jobs.
# OR make a payload work without selenium or playwright

# TODO:
# Have more variables. The filenames could be variables instead.
# Organize the code. Hard to remember how to use it or what to edit.
# Have "users.json": Where you can add users with job seareching criteria's.
# Look at more forms. To find more forms.
# Try to make playwright work with any forms.
# It should find the form element. And see everything inside of it.
# Read labels or text inside.
# If forms can not be understood, use AI to read the form. Like a fallback.

# TODO: (Emma)
# Have checkboxes next to the jobs. If they are checked, it means the job was applied.
# Press a button to run: rapportering().

todayDate = datetime.datetime.now().date() # Todays date
# month = todayDate.month
# theFile = r"unpack\jobtechdev\minio\arkiv\output.json" # File Location for the Json file.
theFile = os.path.join("unpack", "jobtechdev", "minio", "arkiv", "output.json")
# searched_jobs = 'jobs-i-will-apply-for.csv'
searched_jobs = 'job-to-apply.csv'


print("--- Downloading Job Data ---")
print("")
zipDownloader(todayDate) # Downloads it.
print("Done downloading and unzipping.")

# TODO: Make so I can pass more settings. like jobsIwant, blockedEmploieese
print("--- Sorting Job Data ---")
print("")
print(readTheJson(theFile)) # Read from the json


# Opens all the links in the browser.
print("--- Open all URLS's ---")
open_all_urls(searched_jobs)

print("--- Checkboxes ---")
print("")
process_rows(input_file='job-to-apply.csv', output_file='applied_jobs.csv')

# from searched_jobs, auto apply to af.
print("--- Reporting jobs ---")
rapportering() # from: applied_jobs.csv

print("It's done.")
