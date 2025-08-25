# Program to check if a number is prime

num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is not a prime number.")
else:
    is_prime = True  # assume it's prime

    for i in range(2, num):
        if num % i == 0:  # if divisible by any number other than 1 and itself
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
