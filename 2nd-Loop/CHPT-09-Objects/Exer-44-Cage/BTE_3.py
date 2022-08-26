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
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs
    
    def __repr__(self):
        return f"{self.color} {self.species}, {self.number_of_legs} legs"

class Wolf(Animal):
    space_required = 10

    def __init__(self, color):
        super().__init__(color, 4)


class Sheep(Animal):
    space_required = 5

    def __init__(self, color):
        super().__init__(color, 4)

class Snake(Animal):
    space_required = 2

    def __init__(self, color):
        super().__init__(color, 0)

class Parrot(Animal):
    space_required = 1

    def __init__(self, color):
        super().__init__(color, 2)

class DangerousAssignmentError(Exception):
    pass

class Cage():
    pass

class BigCage(Cage):
    pass
