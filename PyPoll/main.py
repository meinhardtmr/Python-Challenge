# Author: Mark Meinhardt
# Date: 04/03/23

import os
import csv

#Procedure to write ouput to screen and a file
def write_line(line, writer):
    print(line)
    print()
    writer.writerow([line])
    writer.writerow([])

# Path to collect data from the Resources folder
FILE_NAME = "election_data.csv"
FOLDER_NAME = "Resources"
os_file_path = os.path.join(".", FOLDER_NAME, FILE_NAME)

# Read in the CSV file
with open(os_file_path, newline = '') as csv_file:

    # Split the data on commas
    election_list = csv.reader(csv_file, delimiter=',')
    
    #Skip past header record
    next(election_list)

    # Create new dictionary to hold results
    election_results = {}

    for r in election_list:
       if r[2] in election_results:
            election_results[r[2]] += 1
       else:
            election_results[r[2]] = 1
    
    total_votes = sum(election_results.values())

#Print report to screen and file.
FILE_NAME = "election_results.txt"
FOLDER_NAME = "analysis"
os_file_path = os.path.join(".", FOLDER_NAME, FILE_NAME)

# Open text file for write
with open(os_file_path, 'w', newline = '') as txt_file:
    writer = csv.writer(txt_file)

    print()
    line = "Election Results"
    write_line(line, writer)
    line = "----------------------------"
    write_line(line, writer)
    line = f"Total Votes: {total_votes}"
    write_line(line, writer)
    line = "----------------------------"
    write_line(line, writer)
    
    for key,value in election_results.items():
        line = f"{key}: {round(value/total_votes*100,3)}% ({value})"
        write_line(line, writer)

    line = "----------------------------"
    write_line(line, writer)
    line = f"Winner: {sorted(election_results, key=election_results.get, reverse = True)[0]}"
    write_line(line, writer)
    line = "----------------------------"
    write_line(line, writer)
