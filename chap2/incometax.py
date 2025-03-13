TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTiON = 3000.0

grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

taxable_income = grossIncome - STANDARD_DEDUCTION - \
            DEPENDENT_DEDUCTiON * numDependents
incomeTax = taxable_income * TAX_RATE

print("The income tax is $" + str(round(incomeTax)))