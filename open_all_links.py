import csv
import webbrowser


# file_one = 'job-to-apply.csv'

# csv_file_path = 'jobs-i-will-apply-for.csv'

def open_all_urls(csv_file_path):
    try:
        with open(csv_file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                form_link = row.get('form_link')
                if form_link:
                    webbrowser.open(form_link)
                else:
                    print(f"No form link found for row {reader.line_num}")

    except FileNotFoundError:
        print(f"File '{csv_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")