sideA = float(input("Please enter the measurement of side A: "))
sideB = float(input("Now enter the measurement for side B: "))
sideC = float(input("Finally enter the measurement for side C: "))

if sideA and sideB != sideC:
    print("This is not an equilateral triangle")
else:
    print("This is an equilateral triangle")
input("Press enter to quit!") 