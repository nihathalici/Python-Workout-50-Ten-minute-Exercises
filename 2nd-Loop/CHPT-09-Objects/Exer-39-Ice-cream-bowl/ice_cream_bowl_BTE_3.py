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


