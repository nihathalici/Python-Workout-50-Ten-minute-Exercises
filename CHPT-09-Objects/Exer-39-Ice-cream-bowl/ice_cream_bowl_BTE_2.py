'''
Write a method, Shelf.has_book, that takes a single string argument and returns
True or False, depending on whether a book with the named title exists on the
shelf.
'''

class Book():
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

class Shelf():
    def __init__(self):
        self.books = []

    def add_book(self, *args):
        self.books += args

    def total_price(self):
        return sum(one_book.price
                   for one_book in self.books)

    def has_book(self, title):
        return title in (one_book.title
                         for one_book in self.books)

    def __repr__(self):
        return '\n'.join(b.title
                         for b in self.books)
        

b1 = Book('Foundation', 'Isaac Asimov', 9)
b2 = Book('Dune', 'Frank Herbert', 12)
b3 = Book('Nineteen Eighty-Four', 'George Orwell', 15)

s = Shelf()
s.add_book(b1, b2)
s.add_book(b3)

print(s.has_book('Foundation'))
