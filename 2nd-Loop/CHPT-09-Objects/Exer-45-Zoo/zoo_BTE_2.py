
'''
As things currently stand, we’re treating our Zoo class almost as if it’s
a singleton object—that is, a class that has only one instance. What a sad
world that would be, with only one zoo! Let’s assume, then, that we have two
instances of Zoo, representing two different zoos, and that we would like
to transfer an animal from one to the other. Implement a Zoo.transfer_animal
method that takes a target_zoo and a subclass of Animal as arguments.
The first animal of the specified type is removed from the zoo on which
we’ve called the method and inserted into the first cage in the target zoo.
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
    def __init__(self):
        self.cages = []
    
    def add_cages(self, *cages):
        for one_cage in cages:
            self.cages.append(one_cage)
    
    def __repr__(self):
        return '\n'.join(str(one_cage)
                         for one_cage in self.cages)
    
    def animals_by_color(self, color):
        return [one_animal
                for one_cage in self.cages
                for one_animal in one_cage.animals
                if one_animal.color == color]
    
    def animals_by_legs(self, number_of_legs):
        return [one_animal
                for one_cage in self.cages
                for one_animal in one_cage.animals
                if one_animal.number_of_legs == number_of_legs]
    
    def number_of_legs(self):
        return sum(one_animal.number_of_legs
                   for one_cage in self.cages
                   for one_animal in one_cage.animals)
    
    def transfer_animal(self, target_zoo, species):
        for one_cage in self.cages:
            for one_animal in one_cage.animals:
                if isinstance(one_animal, species):
                    one_cage.remove(one_animal)
                    target_zoo.cages[0].add_animals(one_animal)

wolf = Wolf('black')
sheep = Sheep('white')
snake = Snake('brown')
parrot = Parrot('green')

c1 = Cage(1)
c1.add_animals(wolf, sheep)

c2 = Cage(2)
c2.add_animals(snake, parrot)

z = Zoo()
z.add_cages(c1, c2)

print(z)
print(z.animals_by_color('white'))
print(z.animals_by_legs(4))
print(z.number_of_legs())
