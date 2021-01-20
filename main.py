""" Calculate cost of production - Econ """

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
file = open('CoP Answer Sheet.csv', 'w', newline="")
if (file == None):
    exit(3)

csvReader = csv.DictReader(database)
fieldnames = ['Magazine per month','Total fixed costs','Total Variable costs','Total costs','Average costs','Marginal cost','Total Revenue','Total profit']
csvWriter = csv.DictWriter(file, fieldnames=fieldnames)

csvWriter.writeheader()

# Prompt for FC, VC and price
fixedCost = int(input("Enter fixed cost: "))
variableCost = int(input("Enter variable cost: "))
price = int(input("Enter price: "))

for row in csvReader:
    # Variable for each field
    output = int(row['Magazine per month'].lower())
    FC = row['Total fixed costs'].lower()
    VC = row['Total Variable costs'].lower()
    totalCost = row['Total costs'].lower()
    avgCost = row['Average costs'].lower()
    marginalCost = row['Marginal cost'].lower()
    totalRevenue = row['Total Revenue'].lower()
    totalProfit = row['Total profit'].lower()

    # Calculate fixed cost
    if FC == "":
        row['Total fixed costs'] = fixedCost

    # Calculate variable cost
    if VC == "":
        VC = variableCost * output
        row['Total Variable costs'] = VC

    # Calculate total cost
    if totalCost == "":
        totalCost = fixedCost + VC
        row['Total costs'] = totalCost
        
    # Calculate average cost
    if avgCost == "":
        avgCost = totalCost // output
        row['Average costs'] = avgCost

    # Calculate marginal cost
    if marginalCost == "":
        marginalCost = (totalCost - previousTC)/(output - previousOutput)
        row['Marginal cost'] = marginalCost
        
    # Calculate total revenue
    if totalRevenue == "":
        totalRevenue = price * output
        row['Total Revenue'] = totalRevenue
       
    # Calculate total profit
    if totalProfit == "":
        totalProfit = totalRevenue - totalCost
        row['Total profit'] = totalProfit

    # Values from previous iteration(output & total cost)
    previousOutput = output
    previousTC = totalCost


    csvWriter.writerow(row)

# Close files
database.close()
file.close()


