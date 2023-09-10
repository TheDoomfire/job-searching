import datetime
# import download_jobtechdev # My file
from download_jobtechdev import zipDownloader
from use_jobtechdev import readTheJson
# import use_jobtechdev # My file

# Run only this file.

# BIG TODO
# Make playwright auto applying the jobs.
# OR make a payload work without selenium or playwright

# Todo
# Playwright arbetsformedlingen aktivitetsrapportera
# Temporarly from csv file.



todayDate = datetime.datetime.now().date() # Todays date
# month = todayDate.month
theFile = r"unpack\jobtechdev\minio\arkiv\output.json" # File Location for the Json file.


print("--- Downloading Job Data ---")
print("")
zipDownloader(todayDate) # Downloads it.
print("Done downloading and unzipping.")
print("--- Sorting Job Data ---")
print("")
print(readTheJson(theFile)) # Read from the json

print("It's done.")