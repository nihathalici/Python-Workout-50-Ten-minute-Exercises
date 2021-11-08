'''
Modify your Book class such that it adds another attribute, width. Then add
a width attribute to each instance of Shelf. When add_book tries to add books
whose combined widths will be too much for the shelf, raise an exception.
'''

class Book():
    def __init__(self, title, author, price, width):
        self.title = title
        self.author = author
        self.price = price
        self.width = width

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
    def total_width(self):
        return sum(one_book.width
                   for one_book in self.books)

    def total_width(self):
        return sum(one_book.width
                   for one_book in self.books)

    def __repr__(self):
        return '\n'.join(b.title
                         for b in self.books)
        

b1 = Book('Foundation', 'Isaac Asimov', 9, 3)
b2 = Book('Dune', 'Frank Herbert', 12, 5)
b3 = Book('Nineteen Eighty-Four', 'George Orwell', 15, 2)

s = Shelf()
s.add_book(b1, b2)
s.add_book(b3)

print(s.total_width())
