#Mini Project (Combine Concepts) - Build a Library Management System:
   #- Book class with title, author, available_copies.
   #- Library class to manage a collection of books (add, borrow, return).
   #- Handle cases where a book is not available with exceptions.


class Book:
    def __init__(self, title, author, available_copies):
        self.title = title
        self.author = author
        self.available_copies = available_copies

    def __str__(self):
        return f"{self.title} by {self.author} ({self.available_copies} copies available)"


class BookNotAvailableError(Exception):
    pass


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.available_copies > 0:
                    book.available_copies -= 1
                    print(f"You borrowed '{book.title}'")
                    return
                else:
                    raise BookNotAvailableError("No copies left!")
        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available_copies += 1
                print(f"You returned '{book.title}'")
                return
        print("Book not found.")


# Usage
library = Library()
library.add_book(Book("Python 101", "sameeullah", 3))
library.add_book(Book("AI Basics", "muhammad umair", 2))

library.borrow_book("Python 101")
library.borrow_book("Python 101")
library.return_book("Python 101")

for b in library.books:
    print(b)
