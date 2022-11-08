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


def zipDownloader(theDate):
    count = -1
    isTrue = True
    while(isTrue != True):
        yestoday = todayDate + datetime.timedelta(count) # -1 means - 1 day.
        count = count -1
        fileName = f"{yestoday}.tar.gz" 
        downloadUrl = f"https://data.jobtechdev.se/annonser/jobtechlinks/{fileName}"
        req = requests.get(downloadUrl) # Downloads it.

        # Downloads it. ??
        with open(fileName, "wb") as f:
            for chunk in req.iter_content(chunk_size=8192): # Download it in chunks if its too big.
                if chunk:
                    f.write(chunk)


        if os.path.getsize(fileName) < 50000:
            os.remove(fileName)
            isTrue = False
        else:
            isTrue = True

zipDownloader(todayDate)

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

# Dosent work with .tar.gz files.
""" with zipfile.ZipFile(fileName) as zip_object: # Unzips the file. Default is "r"
    zip_object.extractall("unpack") """

#tarfile
""" with tarfile.open(fileName) as zip_object: # Unzips the file. Default is "r"
    zip_object.extractall("./unpack") """

""" print(fileName)
file = tarfile.open(fileName)
print(file)
file.extractall("./unpack")
file.close()
 """



# os.getcwd() # Sets the path to the current working folder. Otherwise from C://

# patoolib.extract_archive(fileName, outdir="unpack") # Unzips it to the folder = outdir, it HAS to exist.