#Program to find the second largest number in a list#

def second_largest(numbers):
    # Remove duplicates first (optional)
    unique_numbers = list(set(numbers))
    
    # Sort the list in descending order
    unique_numbers.sort(reverse=True)
    
    # Check if we have at least 2 numbers
    if len(unique_numbers) < 2:
        return "No second largest number"
    else:
        return unique_numbers[1]

# Example usage
my_list = [12, 5, 20, 8, 20, 15]
print("Second largest number is:", second_largest(my_list))
