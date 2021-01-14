from sys import argv, exit
import csv

# Check for command-line args
if len(argv) != 2:
    print("Error")
    exit(1)

# Open the csv file
database = open(argv[1], "r")

# Create DictReader
reader = csv.DictReader(database)

# Prompt for FC
fixedCost = int(input("Enter fixed cost: "))

# Iterate over CSV file, printing each title
for row in reader:
    FC = row["Total fixed costs"]
    
    if FC in row:
        database.append(fixedCost)
        print(FC)

# 1.Create a dictionary of the database (read contents into memory)
#   Create list of the particular STRs
STRs = []

person = {}
for name, data in enumerate(database):
    if name == 0:
        # Generate list of STR using for loop
        STRs = [x for x in data.strip().split(",")][1:]  # output not included
        FC = name["Total fixed costs"]
        print(STRs)
    else:
        if FC in row:
            database.append(fixedCost)
            print(FC)