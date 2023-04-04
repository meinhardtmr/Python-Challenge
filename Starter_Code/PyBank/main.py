# Author: Mark Meinhardt
# Date: 04/03/23

import os
import csv
from operator import itemgetter

#Procedure to write output to screen and file
def write_line(line, writer):
    print(line)
    print()
    writer.writerow([line])
    writer.writerow([])

# Path to collect data from the Resources folder
FILE_NAME = "budget_data.csv"
FOLDER_NAME = "Resources"
os_file_path = os.path.join(".", FOLDER_NAME, FILE_NAME)

# Read in the CSV file
with open(os_file_path, newline = '') as csv_file:

    # Split the data on commas
    budget_list = list(csv.DictReader(csv_file, delimiter=','))

data_list = []
total = 0
change = 0

for r in range(len(budget_list)):
    total += int(budget_list[r]["Profit/Losses"])
    if r > 0:
        value = int(budget_list[r]["Profit/Losses"]) - int(budget_list[r-1]["Profit/Losses"])
        data_list.append([budget_list[r]["Date"], value])
        change += value
    
#Sort list to get greatest and least greatest increases in profits.
data_list = sorted(data_list, key=itemgetter(1), reverse = True) 

#Print report to screen and file.
FILE_NAME = "financial_analysis.txt"
FOLDER_NAME = "analysis"
os_file_path = os.path.join(".", FOLDER_NAME, FILE_NAME)

# Open file for write
with open(os_file_path, 'w', newline = '') as txt_file:
    writer = csv.writer(txt_file)

    print()
    line = "Financial Analysis"
    write_line(line, writer)
    line = "----------------------------"
    write_line(line, writer)
    line = f"Total Months: {len(budget_list)}"
    write_line(line, writer)
    line = f"Total: ${total}"
    write_line(line, writer)
    line = f"Average Change: ${round(change/len(data_list),2)}"
    write_line(line, writer)
    line = f"Greatest Increase in Profits: {data_list[0][0]} (${data_list[0][1]})"
    write_line(line, writer)
    line = f"Greatest Decrease in Profits: {data_list[len(data_list)-1][0]} (${data_list[len(data_list)-1][1]})"
    write_line(line, writer)
