""" Calculate cost of production - Econ """

from sys import argv, exit
import csv

# Check for command-line args
if len(argv) != 3:
    print("Error")
    exit(1)

# Open the csv file
database = open(argv[2], "r")

# Answer Sheet
file = open('CoP Answer Sheet.csv', 'w')
if (file == None):
    exit(1)

# Create DictReader
reader = csv.DictReader(database)

# Prompt for FC, VC and price
fixedCost = int(input("Enter fixed cost: "))
variableCost = int(input("Enter variable cost: "))
price = int(input("Enter price: "))

# Write the fieldnames/column names in row 0
for i in range(len(reader.fieldnames)):
    file.write(reader.fieldnames[i] + ',')
file.write("\n")

# Iterate over each row and input data
for row in reader: 
    # Variable for data of given row
    output = int(row['Magazine per month'].lower())
    FC = row['Total fixed costs'].lower()
    VC = row['Total Variable costs'].lower()
    totalCost = row['Total costs'].lower()
    avgCost = row['Average costs'].lower()
    marginalCost = row['Marginal cost'].lower()
    totalRevenue = row['Total Revenue'].lower()
    totalProfit = row['Total profit'].lower()

 
    # Output
    file.write((str(output) + ","))

    # Calculate fixed cost
    if FC == "":
        FC = fixedCost
        file.write("%i," % (FC))

    # Calculate variable cost
    if VC == "":
        VC = variableCost * output
        file.write("%i," % (VC))
        
    # Calculate total cost
    if totalCost == "":
        totalCost = FC + VC
        file.write("%i," % (totalCost))
        
    # Calculate average cost
    if avgCost == "":
        avgCost = totalCost / output
        file.write("%i," % (avgCost))

    # Avg cost in the first row
    if avgCost == "-":
        file.write("-,")

    # Calculate marginal cost
    if marginalCost == "":
        marginalCost = (totalCost - previousTC)/(output - previousOutput)
        file.write("%i," % (marginalCost))

    # Marginal cost in the first row
    if marginalCost == "-":
        file.write("-,")
        
    # Calculate total revenue
    if totalRevenue == "":
        totalRevenue = price * output
        file.write("%i," % (totalRevenue))
        
    # Calculate total profit
    if totalProfit == "":
        totalRevenue = totalRevenue - totalCost
        file.write("%i" % (totalRevenue))   


    # Values from previous iteration(output & total cost)
    previousOutput = output
    previousTC = totalCost

    # Move to next line for next iteration
    file.write("\n")


# Close files
database.close()
file.close()
