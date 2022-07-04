import csv

with open("jobs.csv") as f:
    reader = csv.DictReader(f)

    count = 0

    for row in reader:
        print(row["jobb"])

        if count > 4:
            break

        count +=1