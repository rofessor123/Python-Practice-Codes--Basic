# Operator Overloading : Create a Vector class that supports addition (+) of two vectors. 

#Operator overloading lets us define how operators work with custom objects. Example: + between vectors.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # overloading +
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
print(v1 + v2)  
