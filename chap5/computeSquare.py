"""
Illustrates the definition of a main function.
"""

def main():
    """The main function for this script"""
    number = float(input("Enter a number: "))
    result = square(number)
    print("The square of", number, "is", result)

def square(x):
    """Returns the squre of x."""
    return x * x


if __name__ == "__main__":
    main()