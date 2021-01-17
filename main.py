from sys import argv, exit
import csv


# Open the csv file
database = open(argv[1], "r")

# Answer Sheet
file = open('Answer Sheet.csv', 'w')
if (file == None):
    exit(1)

# Create DictReader
reader = csv.DictReader(database)

# Prompt for FC
fixedCost = int(input("Enter fixed cost: "))
variableCost = int(input("Enter variable cost: "))
price = int(input("Enter profit: "))


for row in reader: 
    output = int(row['Magazine per month'].lower())
    FC = row['Total fixed costs'].lower()
    VC = row['Total Variable costs'].lower()
    totalCost = row['Total costs'].lower()
    avgCost = row['Average costs'].lower()
    marginalCost = row['Marginal cost'].lower()
    totalRevenue = row['Total Revenue'].lower()
    totalProfit = row['Total profit'].lower()

    if FC == "":
        FC = fixedCost
        file.write("%i," % (FC))

    if VC == "":
        VC = variableCost * output
        file.write("%i," % (VC))

    if totalCost == "":
        totalCost = FC + VC
        file.write("%i," % (totalCost))

    if avgCost == "":
        avgCost = totalCost / output
        file.write("%i," % (avgCost))

    if marginalCost == "":
        marginalCost = (totalCost - previousTC)/(output - previousOutput)
        file.write("%i," % (marginalCost))

    if totalRevenue == "":
        totalRevenue = price * output
        file.write("%i," % (totalRevenue))

    if totalProfit == "":
        totalRevenue = totalRevenue - totalCost
        file.write("%i" % (totalRevenue))   

    previousOutput = output
    previousTC = totalCost
    file.write("\n")

database.close()
file.close()


