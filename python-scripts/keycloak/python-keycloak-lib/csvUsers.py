# read in the CSV
# for each row
#    for each column
#       print the value to the screen
import csv

csv_file = 'users.csv'

with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        print(row[0].strip(),"\n", row[1].strip(),"\n", row[2].strip(),"\n", row[3].strip(), sep='')