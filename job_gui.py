import csv
import webbrowser

def process_rows(input_file='jobs-to-apply.csv', output_file='applied_jobs.csv'):
    # Load data from CSV
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    completed_rows = []
    
    print("\n" + "="*50)
    print("Starting row processing (press Enter after each action)")
    print("="*50)
    
    for i, row in enumerate(rows, 1):
        # Determine which link to use
        link = row['form_link'] if row['form_link'] else row['job_link']
        af_link = row['af_link']
        
        print(f"\n--- Row {i}/{len(rows)} ---")
        print(f"Title: {row['title']}")
        print(f"Primary Link: {link}")
        print(f"AF Link: {af_link}")
        
        while True:
            action = input("Actions: [v]iew link, [m]ark complete, [s]kip, [q]uit: ").strip().lower()
            
            if action == 'v':
                if link:
                    webbrowser.open(link)
                else:
                    print("No link available!")
            elif action == 'm':
                completed_rows.append(row)
                print("Marked as completed ✓")
                break
            elif action == 's':
                print("Skipped")
                break
            elif action == 'q':
                print("Exiting early...")
                return save_completed(completed_rows, output_file)
            else:
                print("Invalid option. Please choose v, m, s, or q")
    
    return save_completed(completed_rows, output_file)

def save_completed(rows, output_file):
    if not rows:
        print("\nNo rows were marked as completed")
        return False
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"\nSaved {len(rows)} completed rows to {output_file}")
    return True

# Example usage in your main script:
# if __name__ == "__main__":
#     # Your existing code that generates the initial CSV
#     # ...
#     
#     # Process rows
#     process_rows('your_input.csv', 'completed.csv')
#     
#     # Continue with your script
#     print("Continuing with the rest of the script...")
