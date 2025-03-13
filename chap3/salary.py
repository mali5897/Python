"""
This app takes the input for starting salary, 
the percentage of salary increase, 
and for an amount of years supplied by the user.
It takes the input and displays it in a tabular format, 
showing the increase in salary each year.
"""

salary = float(input("Please enter your salary: "))
payRaise = float(input("What is the percentage of your raise each year?: "))
years = int(input("How many years do you plan on staying?: "))

payRaise = payRaise / 100

raiseAmnt = 0.0

print("%4s %6s" % ("Year", "Salary"))

for year in range(1, years + 1):
    raiseAmnt = (salary * payRaise) + salary
    salary = raiseAmnt
    print("%4d %6.2f" % (year, salary))