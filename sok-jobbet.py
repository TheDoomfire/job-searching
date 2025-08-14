import csv
from datetime import date
import requests
#from this import d
from bs4 import BeautifulSoup



#Eftersom man ska jobbsöka för förra månaden.
today = date.today()
if today.month == 1:
    next_month = "december"
elif today.month == 2:
    next_month = "januari"
elif today.month == 3:
    next_month = "februari"
elif today.month == 4:
    next_month = "mars"
elif today.month == 5:
    next_month = "april"
elif today.month == 6:
    next_month = "maj"
elif today.month == 7:
    next_month = "juni"
elif today.month == 8:
    next_month = "juli"
elif today.month == 9:
    next_month = "agusti"
elif today.month == 10:
    next_month = "september"
elif today.month == 11:
    next_month = "oktober"
elif today.month == 12:
    next_month = "november"


def get_jobs():
    with open("jobs.csv") as f:
       reader = csv.DictReader(f)

       for row in reader:
         #Gets all jobs fom next_month
         #if next_month in row["tid"]:
           print(row["link"])


get_jobs()

