import csv

# Open the CSV file
with open('Astrocsv3.csv', newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    
    # Skip the header row
    next(reader)

    # Initialize lists to store the values
    SaturnLong = []
    Mars = []
    DateTime = []

    # Iterate through each row in the CSV
    for row in reader:
        if len(row) >= 3:  # Ensure the row has at least 3 columns
            try:
                # Append values to respective lists
                SaturnLong.append(float(row[1]))  # Assuming SaturnLong is the second column
                Mars.append(float(row[2]))        # Assuming Mars is the third column
                DateTime.append(row[0])           # Assuming Date Time is the first column
            except ValueError as e:
                print(f"Error converting row: {row} -> {e}")
                continue
        else:
            print(f"Skipping incomplete row: {row}")

    # Calculate differences
    differences = [saturn - mars for saturn, mars in zip(SaturnLong, Mars)]

# Print the results
for date_time, diff in zip(DateTime, differences):
    print(f"Date Time: {date_time}, Difference: {diff}")
    
# I want to check for differences 30 and its date

