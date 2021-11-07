'''
Create a Book class that lets you create books with a title, author, and price.
Then create a Shelf class, onto which you can place one or more books with an
add_book method. Finally, add a total_price method to the Shelf class, which
will total the prices of the books on the shelf.
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

    def __repr__(self):
        return '\n'.join(b.title
                         for b in self.books)
        

b1 = Book('Foundation', 'Isaac Asimov', 9)
b2 = Book('Dune', 'Frank Herbert', 12)
b3 = Book('Nineteen Eighty-Four', 'George Orwell', 15)

s = Shelf()
s.add_book(b1, b2)
s.add_book(b3)

print(s)
