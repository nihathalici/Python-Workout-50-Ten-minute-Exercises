'''
Our zookeepers have a macabre sense of humor when it comes to placing animals together,
in that they put wolves and sheep in the first cage, and snakes and birds in the other
cage. (The good news is that with such a configuration, the zoo will be able to save
on food for half of the animals.) Define a dict describing which animals can be with others.
The keys in the dict will be classes, and the values will be lists of classes that can
compatibly be housed with the keys. Then, when adding new animals to the current cage,
you’ll check for compatibility. Trying to add an animal to a cage that already contains
an incompatible animal will raise an exception.
'''
class Animal():
    pass

class Wolf(Animal):
    pass

class Sheep(Animal):
    pass

class Snake(Animal):
    pass

class Parrot(Animal):
    pass

class DangerousAssignmentError(Exception):
    pass

class Cage():
    pass

class BigCage(Cage):
    pass