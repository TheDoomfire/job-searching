import requests
import datetime
# import patoolib # patoolib
import os
# import zipfile
import shutil
import tarfile



# This program is to download all the job

# TODO
# Download https://data.jobtechdev.se/annonser/jobtechlinks/2022-07-31.tar.gz - DONE
# Access the json file
# Make it able to download the next next days if it dosent exist.

# Get Help
# helpMe = help(datetime.date)

# Check if filesize > 42865924
# if not, change date -1 and try again.


todayDate = datetime.datetime.now().date() # Todays date


def downloadTar(tarFile): # Unzips the file
    with tarfile.open(tarFile) as zip_object: # Unzips the file. Default is "r"
        zip_object.extractall("./unpack")


def zipDownloader(theDate):
    count = -1
    isTrue = False
    while(isTrue == False): # Loops till its true
        myDate = todayDate + datetime.timedelta(count) # -1 means - 1 day.
        count = count -1
        fileName = f"{myDate}.tar.gz" 
        downloadUrl = f"https://data.jobtechdev.se/annonser/jobtechlinks/{fileName}"
        req = requests.get(downloadUrl) # Downloads it.

        # Downloads it. ??
        with open(fileName, "wb") as f:
            for chunk in req.iter_content(chunk_size=8192): # Download it in chunks if its too big.
                if chunk:
                    f.write(chunk)


        if os.path.getsize(fileName) < 50000: # May have to change this.
            os.remove(fileName)
            isTrue = False
        else:
            isTrue = True
            downloadTar(fileName)


# zipDownloader(todayDate)