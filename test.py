from sys import argv, exit
import csv

# Check for command-line args
if len(argv) != 2:
    print("Error")
    exit(1)

# Open the csv file
database = open(argv[1], "r")
if (database == None):
    exit(2)

# Answer Sheet
file = open(argv[1], 'w')
if (file == None):
    exit(3)

csvReader = csv.DictReader(database)
fieldnames = ['Magazine per month','Total fixed costs','Total Variable costs','Total costs','Average costs','Marginal cost','Total Revenue','Total profit']
csvWriter = csv.DictWriter(file, fieldnames=fieldnames)

csvWriter.writeheader()
for row in csvReader:
    csvWriter.writerow(row)