
'''
Rather than write a helper, you could also define iteration capabilities in a class
and then inherit from it. Reimplement Circle as a class that inherits from CircleIterator,
which implements __init__ and __next__. Of course, the parent class will have to know
what to return in each iteration; add a new attribute in Circle, self.returns, a list of
attribute names that should be returned.
'''

class CircleIterator():
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times
        self.index = 0
    
    def __next__(self):
        if self.index >= self.max_times:
            raise StopIteration
        
        iterated_data = getattr(self, self.returns)

        value = iterated_data[self.index % len(iterated_data)]
        self.index += 1
        return value
    
    def __iter__(self):
        return type(self)(self.data, self.max_times)


class Circle(CircleIterator):
    def __init__(self, data, max_times):
        super().__init__(data, max_times)
        self.returns = 'data'

c = Circle('abcd', 7)

print('** A **')
for one_item in c:
    print(one_item)

print('** B **')
for one_item in c:
    print(one_item)
