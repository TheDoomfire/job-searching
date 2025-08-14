import csv
import webbrowser

# Open links

with open("job-to-apply.csv") as f:
    reader = csv.reader(f)
    count = 0
    next(reader) # Skips the header row

    for row in reader:
        link = row[5]
        webbrowser.open_new(link)
        #print(link)
        if count > 10:
            break
        count += 1


# webbrowser.open("https://chooseinvesting.com/", new=0, autoraise=True)


print("Done.")