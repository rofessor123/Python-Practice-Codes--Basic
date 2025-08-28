#Inheritance - Create a Person class with 
# attributes: name, age. Create a Student 
# subclass that inherits from Person and 
# adds student_id.#

#parent class

# Parent class
class Person:
    def __init__(self, name, age):   # Constructor of Person
        self.name = name
        self.age = age

    def show_info(self):  # Method to display person info
        return f"Name: {self.name}, Age: {self.age}"


# Child class (inherits from Person)
class Student(Person):
    def __init__(self, name, age, student_id):
        # Call the constructor of Person (parent class)
        super().__init__(name, age)  
        self.student_id = student_id

    def show_student_info(self):  # Method for student info
        return f"{self.show_info()}, Student ID: {self.student_id}"


# Example usage:
p1 = Person("Ali", 30)
print(p1.show_info())

s1 = Student("Ayesha", 21, "ST1234")
print(s1.show_student_info())




