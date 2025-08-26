#Fibonacci sequence up to n terms
#The first two numbers are always 0 and 1.
#Every number after that is the sum of the two 
# numbers before it.

def fibonacci(n):
    sequence = [0, 1]  # First two numbers
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])  # add last two numbers
    return sequence[:n]


print(fibonacci(7))  # [0, 1, 1, 2, 3, 5, 8]
