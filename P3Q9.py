#Iterator - Create a custom iterator class that generates squares of numbers up to n.

# Theory: Iterators allow objects to be looped with for. Custom iterators need __iter__() and __next__().

class SquareIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration

squares = SquareIterator(5)
for num in squares:
    print(num)  # 1, 4, 9, 16, 25