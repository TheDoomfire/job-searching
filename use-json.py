import json
import pandas as pd
import datetime


todayDate = datetime.datetime.now().date() # Todays date


theFile = "output.json" # File Location for the Json file.
jobsIwant = ["data", "programerare", "it-strateg", "systemutvecklare", "data engineer", "data analyst", "truckförare", "lagerarbetare", ]
whereIwantJob = "örebro"
ignoreEmployers = ["dhl", "tranpenad"]


# Load every line into data. So data = jsonFile
data = [json.loads(line) for line in open(theFile,'r', encoding="utf8")]


# TODO
# add all jobs in a json file if not already in there. Sort by month?
# Combine this and download-json.py so it downloads it and then open up the file and running this program.

joblist = []
myNumber = 0
for myNumber in range(len(data)):
    try:
        jobLocation = data[myNumber]["originalJobPosting"]["jobLocation"]["addressLocality"] # City adress
        jobTitle = data[myNumber]["originalJobPosting"]["title"]
        JobOccupation = data[myNumber]["originalJobPosting"]["relevantOccupation"]["name"] # Job title
        hiringOrganizationName = data[myNumber]["originalJobPosting"]["hiringOrganization"]["name"] # Name of the Hirining Company
        jobLink = data[myNumber]["original_source_links"][0]["link"] # For the job ad
        jobValid = data[myNumber]["originalJobPosting"]["validThrough"] # when it expires

        if jobLocation.casefold() == whereIwantJob.casefold(): # .casefold is like .lower but apperently better.
            if any(work_title in JobOccupation.casefold() for work_title in jobsIwant):
                if not any(work_title in hiringOrganizationName.casefold() for work_title in ignoreEmployers):
                    if str(todayDate) < str(jobValid): # Checks to see if I can still apply for it.
                        print(jobLocation)
                        print(JobOccupation)
                        print(hiringOrganizationName)
                        print(jobLink)
                        print(jobTitle)
                        print(myNumber)
                        print("Today: ", todayDate)
                        print(jobValid)
                        job = {"occupation": JobOccupation, 
                        "organization": hiringOrganizationName, 
                        "title": jobTitle, 
                        "link": jobLink}
                        joblist.append(job)
                        
                    # if hiringOrganizationName.casefold() in ignoreEmployers.casefold():
                    # any(work_title in JobOccupation.casefold() for work_title in jobsIwant.casefold())
    except Exception: # If ANY error in the code. Skips and continues with the loop
        continue


    # "occupationalCategory" or "name" in ["hiringOrganization"]
    # if name in "hiringOrganization" error. ??

# Add to a CSV file.
""" df = pd.DataFrame(joblist)
df.to_csv("job-to-apply.csv") """

# Working perfect.
""" if jobLocation.casefold() == "örebro": # .casefold is like .lower but apperently better.
    test = True
else:
    test = False """
