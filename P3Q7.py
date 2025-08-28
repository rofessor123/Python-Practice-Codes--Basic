#Exception Handling - Write a program that takes input from the user and raises a custom exception if the input is negative.


#We can raise custom exceptions if invalid input occurs.

class NegativeNumberError(Exception):
    pass

def check_number(num):
    if num < 0:
        raise NegativeNumberError("Negative number is not allowed!")
    else:
        print(f"Valid number: {num}")

try:
    n = int(input("Enter a number: "))
    check_number(n)
except NegativeNumberError as e:
    print("Error:", e)