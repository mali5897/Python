"""
Payroll application that reads employee
data from a file and outputs the 
payroll summary in tabular format
"""

import time
import os.path

fileName = input("Enter the pay roll file name please: ")

# while loop which is used to validate the input, making sure that the file name the user types actually exists

while os.path.isfile(fileName) == False:
    fileName = input("That was the wrong file name, please try again: ")

# Out of the loop means the filename is valid

print("Processing payroll file data ...")
time.sleep(2)

# Processing and output phases

data = open(fileName, "r")

print()
print("%-18s%9s%9s%11s" % ("Last Name", " Wage", "Hours", "Earnings"))
print("-" * 50)

# For loop to go through the file line by  line. Split up the data in each line and place each component into tabular format and calculate the earnings.

for line in data:
    # Break the line into individual starting values
    dataArray = line.split()
    # extract the last name from that array and store it
    name = dataArray[0]
    # Extract the wage from the array, convert it to a float and store
    wage = float(dataArray[1])
    # Extract the hours from the array, convert it to float and store it
    hours  = float(dataArray[2])
    # Next calculate the earnings and store it 
    earnings = wage * hours 
    # Output the info into the tabular format
    print("%-18s%9.2f%9.2f%11.2f" % (name, wage, hours, earnings))

print("-" * 50)










