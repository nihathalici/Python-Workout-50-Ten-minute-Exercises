'''
Modify animals_by_color such that it takes any number of colors. Animals
having any of the listed colors should be returned. The method should raise
an exception if no colors are passed.
'''

class Animal():
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs
    
    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'

class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)

class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)

class Cage():
    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []
    
    def add_animals(self, *animals):
        for one_animal in animals:
            self.animals.append(one_animal)
    
    def __repr__(self):
        output = f'Cage {self.id_number}\n'
        output += '\n'.join('\t' + str(animal)
                             for animal in self.animals)
        return output

class NoColorsPassedError(Exception):
    pass

class Zoo():
    pass

