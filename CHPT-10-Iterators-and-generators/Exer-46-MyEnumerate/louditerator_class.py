
class LoudIterator():
    def __init__(self, data):
        '''Store the data in an attribute, self.data'''
        print('\tNow in __init__')
        self.data = data
        # Creates an index attribute,
        # keeping track of our current position
        self.index = 0

    def __iter__(self):
        '''Our __iter__ does the simplest thing, returning self.'''
        print('\tNow in __iter__')
        return self

    def __next__(self):
        print('\tNow in __next__')
        # Raises StopIteration if our self.index
        # has reached the end
        if self.index >= len(self.data):
            print(
                f'\tself.index ({self.index}) is too big; exiting')
            raise StopIteration

        # Grabs the current value,
        # but doesn't return it yet
        value = self.data[self.index]
        # Increments self.index
        self.index += 1
        print('\tGot value {value}, incremented index to {self.index}')
        return value

for one_item in LoudIterator('abc'):
    print(one_item)
        
