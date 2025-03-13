"""
This is a python application that provides an investment report.
User input provides the details of the investment.
Output is the calculation for each year of the investment with totals at the end.

"""





startBalance = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years: "))
rate = float(input("enter the rate as a %: "))

rate = rate / 100

totalInterest = 0.0

print("%4s%18s%10s%16s" % ("Year", "Starting balance", "Interest", "Ending Balance"))


for year in range(1, years + 1):
     interest = startBalance * rate
     endBalance = startBalance + interest
     print("%4d%18.2f%10.2f%16.2f" % (year, startBalance, interest, endBalance))
     startBalance = endBalance
     totalInterest += interest


print("Ending balance : $%0.2f" % endBalance)
print("Total interest earned: $%0.2f" % totalInterest)