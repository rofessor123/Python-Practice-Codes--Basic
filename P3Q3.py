#Encapsulation - Create a BankAccount
#  class with private attribute __balance. 
# Provide methods deposit(), 
# withdraw(), and get_balance().

#Encapsulation means hiding data (making it private)
#  and giving controlled access
#  through methods (functions inside the class).

#In Python, we make an attribute private by 
# writing __ (double underscore) before its name. 
# Example: __balance#

class BankAccount:
    def __init__(self, initial_balance=0):
        # private variable
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)  

account.deposit(500)       
account.withdraw(200)     

print("Current Balance:", account.get_balance())
