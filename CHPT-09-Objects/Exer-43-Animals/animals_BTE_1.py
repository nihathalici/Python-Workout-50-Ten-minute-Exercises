'''
Instead of each animal class inheriting directly, from Animal, define
several new classes, ZeroLeggedAnimal, TwoLeggedAnimal, and FourLeggedAnimal,
all of which inherit from Animal, and dictate the number of legs on each instance.
Now modify Wolf, Sheep, Snake, and Parrot such that each class inherits from one
of these new classes, rather than directly from Animal. How does this affect
your method definitions?
'''



class Animal:
    """Base class for animals."""
    def __init__(self, color):
        self.color = color
        self.species = self.__class__.__name__

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'



class ZeroLeggedAnimal(Animal):
    def __init__(self, color):
        super().__init__(color)
        self.number_of_legs = 0

class TwoLeggedAnimal(Animal):
    def __init__(self, color):
        super().__init__(color)
        self.number_of_legs = 2

class FourLeggedAnimal(Animal):
    def __init__(self, color):
        super().__init__(color)
        self.number_of_legs = 4

class Wolf(FourLeggedAnimal):
     """Class for creating 4-legged wolves of any color"""
     def __init__(self, color):
         super().__init__(color)

class Sheep(FourLeggedAnimal):
    """"Class for creating 4-legged sheep of any color"""
    def __init__(self, color):
        super().__init__(color)

class Snake(ZeroLeggedAnimal):
    """Class for creating 0-legged snakes of any color"""
    def __init__(self, color):
        super().__init__(color)

class Parrot(TwoLeggedAnimal):
    """Class for creating 2-legged parrots of any color"""
    def __init__(self, color):
        super().__init__(color)

unknown_four_legged_animal = FourLeggedAnimal('pink')
wolf = Wolf('black')
sheep1 = Sheep('black')
sheep2 = Sheep('white')
snake = Snake('brown')
parrot = Parrot('green')

print(wolf)
print(sheep1)
print(sheep2)
print(snake)
print(parrot)
print(unknown_four_legged_animal)
