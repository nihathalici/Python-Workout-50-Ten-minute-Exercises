class LoudIterator():
    def __init__(self, data):
        print('\tNow in __init__')
        self.data = data
        self.index = 0

    def __iter__(self):
        print('\tNow in __iter__')
        return self
        
    def __next__(self):
        print('\tNow in __next__')
        if self.index >= len(self.data):
            print(f'\tself.index ({self.index}) is too big; exiting')
            raise StopIteration
        
        value = self.data[self.index]
        self.index += 1
        print('\tGot value {value}, incremented index to {self.index}')
        return value


for one_item in LoudIterator("abc"):
    print(one_item)
