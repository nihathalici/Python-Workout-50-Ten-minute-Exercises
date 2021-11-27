
'''
Rewrite MyEnumerate such that it uses a helper class (MyEnumerateIterator),
as described in the “Discussion” section. In the end, MyEnumerate will have
the __iter__ method that returns a new instance of MyEnumerateIterator,
and the helper class will implement __next__. It should work the same way,
but will also produce results if we iterate over it twice in a row.
'''

class MyEnumerateIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = (self.index, self.data[self.index])
        self.index += 1
        return value

class MyEnumerate():
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return MyEnumerateIterator(self.data) 

for index, letter in MyEnumerate('abc'):
    print(f'{index} : {letter}')
