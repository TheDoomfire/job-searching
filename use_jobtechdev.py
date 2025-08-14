import json
import pandas as pd
import datetime
from webscrape_af import getReferens
from look_for_forms import form_search


# ADDS ALL FROM JSON TO CSV


todayDate = datetime.datetime.now().date() # Todays date
month = todayDate.month
print("Month is: ", month)

# Edit here if you want. Write in lowercase.
theFile = r"unpack\jobtechdev\minio\arkiv\output.json" # File Location for the Json file.

""" # Jobs A want:
jobsIwant = ["data", 
            "programmerare",
            "it-strateg",
            "systemutvecklare",
            "data engineer",
            "data analyst",
            "webb",
            "sökmotoroptimerare",
            "databas",
            "truckförare",
            "lagerarbetare"] #, "butik", "skola" """

# Jobs E wants:
jobsIwant = [
    "hora",
    "marsvin", 
    "virka", 
    "personlig", 
    "boendestödjare", 
    "vårdpersonal", 
    "elevassistent"
    "personligt assistent",
    "städ",
    "städning",
]

whereIwantJob = "örebro"
# whereIwantJob = "kumla"
ignoreEmployers = ["dhl", "tranpenad", "humana"]


# Load every line into data. So data = jsonFile
# data = [json.loads(line) for line in open(theFile,'r', encoding="utf8")]

# TODO
# Remove dublicates in company names.
joblist = []
myNumber = 0
allEmployers = []
def readTheJson(jsonFile):
    data = [json.loads(line) for line in open(jsonFile,'r', encoding="utf8")] # Load every line into data. So data = jsonFile
    for myNumber in range(len(data)):
        try:
            jobLocation = data[myNumber]["originalJobPosting"]["jobLocation"]["addressLocality"] # City adress
            jobTitle = data[myNumber]["originalJobPosting"]["title"]
            JobOccupation = data[myNumber]["originalJobPosting"]["relevantOccupation"]["name"] # Job title
            hiringOrganizationName = data[myNumber]["originalJobPosting"]["hiringOrganization"]["name"] # Name of the Hirining Company
            afLink = data[myNumber]["original_source_links"][0]["link"] # For the job ad
            jobValid = data[myNumber]["originalJobPosting"]["validThrough"] # when it expires
            jobDatePosted = data[myNumber]["originalJobPosting"]["datePosted"]
            firstTime = False
            date_obj = datetime.datetime.strptime(jobDatePosted, "%Y-%m-%d").date()

            if jobLocation.casefold() == whereIwantJob.casefold(): # .casefold is like .lower but apperently better.
                if any(work_title in JobOccupation.casefold() for work_title in jobsIwant):
                    if not any(work_title in hiringOrganizationName.casefold() for work_title in ignoreEmployers):
                        if str(todayDate) < str(jobValid): # Checks to see if I can still apply for it.
                            if (date_obj.month < month) or (month == 1 and date_obj.month == 12): # TEST Checks for only last month. the last or is specifically for january
                                if hiringOrganizationName not in allEmployers: # If not hiringOrganizationName in joblist
                                    tempList = getReferens(afLink)
                                    print(tempList)
                                    jobLink = tempList[0]
                                    form_link = form_search(jobLink)
                                    referens = tempList[1]
                                    job = {"occupation": JobOccupation, 
                                    "organization": hiringOrganizationName, 
                                    "title": jobTitle,
                                    "af_link": afLink,
                                    "job_link": jobLink,
                                    "form_link": form_link,
                                    "referens": referens,
                                    "datePosted": jobDatePosted}
                                    joblist.append(job)
                                    allEmployers.append(hiringOrganizationName)
                                    
                        # if hiringOrganizationName.casefold() in ignoreEmployers.casefold():
                        # any(work_title in JobOccupation.casefold() for work_title in jobsIwant.casefold())
        except Exception: # If ANY error in the code. Skips and continues with the loop
            continue
    # Add to a CSV file.
    if joblist:
        df = pd.DataFrame(joblist)
        df.to_csv("job-to-apply.csv")
        print("Added to CSV")
    return (joblist)
