import datetime
# import download_jobtechdev # My file
from download_jobtechdev import zipDownloader
# import use_jobtechdev # My file

# Run only this file.


todayDate = datetime.datetime.now().date() # Todays date


zipDownloader(todayDate) # Downloads it.


print("Done! Happy run-script")