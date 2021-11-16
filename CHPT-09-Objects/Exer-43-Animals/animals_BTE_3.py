'''
Let’s say that each class’s __repr__ method should print the animal’s sound,
as well as the standard string we implemented previously. In other words,
str(sheep) would be Baa—white sheep, 4 legs. How would you use inheritance
to maximize code reuse?
'''

class Animal:
    """Base class for animals."""

    def __init__(self, color, number_of_legs):
        self.color = color
        self.species = self.__class__.__name__
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.sound}--{self.color} {self.species}, {self.number_of_legs} legs'


class Wolf(Animal):
     """Class for creating x-legged wolves of any color"""

     sound = 'awooo'
     
     def __init__(self, color, number_of_legs):
         super().__init__(color, number_of_legs)
         

class Sheep(Animal):
    """"Class for creating 4-legged sheep of any color"""

    sound = 'baa'
    
    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):
    """Class for creating 0-legged snakes of any color"""

    sound = 'hiss'
    
    def __init__(self, color):
        super().__init__(color, 0)

class Parrot(Animal):
    """Class for creating 2-legged parrots of any color"""

    sound = '\'Polly wants a cracker!\''
    
    def __init__(self, color):
        super().__init__(color, 2)

wolf = Wolf('black', 3)
sheep1 = Sheep('black')
sheep2 = Sheep('white')
snake = Snake('brown')
parrot = Parrot('green')

print(wolf)
print(sheep1)
print(sheep2)
print(snake)
print(parrot)
