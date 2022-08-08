'''
Instead of writing an __init__ method in each subclass, we could also have a
class attribute, number_of_legs, in each subclass—similar to what we did
earlier with Bowl and BigBowl. Implement the hierarchy that way. Do you
even need an __init__ method in each subclass, or will Animal.__init__ suffice?
'''

class Animal:
    def __init__(self, color):
        self.color = color
        self.species = self.__class__.__name__
    
    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'

class Wolf(Animal):
    number_of_legs = 4

    def __init__(self, color):
        super().__init__(color)

class Sheep(Animal):
    number_of_legs = 4

    def __init__(self, color):
        super().__init__(color)

class Snake(Animal):
    number_of_legs = 0

    def __init__(self, color):
        super().__init__(color)

class Parrot(Animal):
    number_of_legs = 2

    def __init__(self, color):
        super().__init__(color)

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

