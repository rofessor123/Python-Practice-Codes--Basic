#Class Basics - Create a Car class with 
# attributes: brand, model, year. 
# Add a method car_info() to
#  display the car details.


        # Defining a class called Car
class Car:
    # Constructor method to initialize the attributes
    def __init__(self, brand, model, year):
        self.brand = brand   # attribute 1
        self.model = model   # attribute 2
        self.year = year     # attribute 3

    # Method to display car details
    def car_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")


# Creating objects (real cars) from the class
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2022)

# Calling the method on each object
car1.car_info()   
car2.car_info()   
