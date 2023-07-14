import datetime
# import download_jobtechdev # My file
from download_jobtechdev import zipDownloader
from use_jobtechdev import readTheJson
# import use_jobtechdev # My file

# Run only this file.

# BIG TODO
# Make selenium auto applying the jobs.
# OR make a payload work without selenium or typewright

# Todo
# Selenium arbetsformedlingen aktivitetsrapportera



todayDate = datetime.datetime.now().date() # Todays date
theFile = r"unpack\jobtechdev\minio\arkiv\output.json" # File Location for the Json file.


# WORKS
zipDownloader(todayDate) # Downloads it.
print(readTheJson(theFile)) # Read from the json


print("Done! Happy run-script")