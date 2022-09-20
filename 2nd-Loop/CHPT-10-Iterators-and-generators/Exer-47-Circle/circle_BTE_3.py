
'''
Implement a MyRange class that returns an iterator that works the same as range,
at least in for loops. (Modern range objects have a host of other capabilities,
such as being subscriptable. Don’t worry about that.) The class, like range,
should
take one, two, or three integer arguments.
'''

class MyRange:
    def __init__(self, first, second=None, step=1):
        if second is None:
            self.current = 0
            self.stop = first
        else:
            self.current = first
            self.stop = second
        self.step = step
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        
        value = self.current
        self.current += self.step
        return value

mr = MyRange(10, 21, 2)

for one_item in mr:
    print(one_item)


