import csv
import webbrowser


with open("job-to-apply.csv") as f:
    reader = csv.reader(f)
    count = 0
    next(reader) # Skips the header row

    for row in reader:
        webbrowser.open_new(row[4])
        print(row[4])
        if count > 6:
            break
        count += 1