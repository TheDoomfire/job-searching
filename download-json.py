import requests
import datetime
import patoolib
import os


# This program is to download all the job

# TODO
# Download https://data.jobtechdev.se/annonser/jobtechlinks/2022-07-31.tar.gz - DONE
# Access the json file

# Get Help
# helpMe = help(datetime.date)


todayDate = datetime.datetime.now().date() # Todays date
yestoday = todayDate + datetime.timedelta(-1) # -1 means - 1 day.
fileName = f"{yestoday}.tar.gz" 
downloadUrl = f"https://data.jobtechdev.se/annonser/jobtechlinks/{fileName}"
req = requests.get(downloadUrl) # Downloads it.


with open(fileName, "wb") as f:
    for chunk in req.iter_content(chunk_size=8192): # Download it in chunks if its too big.
        if chunk:
            f.write(chunk)


# Tried making it a function.
""" def download_file(url, filename=""):
    try:
        if filename: # If filename is not blank
            pass
        else:
            filename = req.url[downloadUrl.rfind("/")+1:]

        with requests.get(url) as req:
            with open(filename, "wb") as f:
                    for chunk in req.iter_content(chunk_size=8192): # Download it in chunks if its too big.
                        if chunk:
                           f.write(chunk)
            return filename
    except Exception as e:
        print(e)
        return None """


os.getcwd() # Sets the path to the current working folder. Otherwise from C://

patoolib.extract_archive(fileName, outdir="unpack") # Unzips it to the folder.