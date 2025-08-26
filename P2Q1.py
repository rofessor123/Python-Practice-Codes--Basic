#Write a function that takes a list and returns the sum of all even numbers#

# Function to calculate sum of even numbers in a list
def sum_of_evens(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:   # check if even
            total += num
    return total

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 10]
print("Sum of even numbers:", sum_of_evens(my_list))
