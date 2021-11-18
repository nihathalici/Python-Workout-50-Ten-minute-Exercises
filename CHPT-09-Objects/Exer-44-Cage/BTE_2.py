'''
It’s not very realistic to say that we would limit the number of animals in
a cage. Rather, it makes more sense to describe how much space each animal
needs and to ensure that the total amount of space needed per animal isn’t
greater than the space in each cage. You should thus modify each of the
Animal subclasses to include a space_required attribute. Then modify the
Cage and BigCage classes to reflect how much space each one has. Adding
more animals than the cage can contain should raise an exception.
'''

class Animal():
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'

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

class NotEnoughSpaceError(Exception):
    pass

class Cage():

    def __init__(self, id_number, total_space):
        self.id_number = id_number
        self.animals = []
        self.total_space = total_space


    def add_animals(self, *animals):
        for one_animal in animals:
            if self.space_used() + one_animal.space_required > self.total_space:
                raise NotEnoughSpaceError(
                    f'Not enough room for your {one_animal}')
            self.animals.append(one_animal)

    def space_used(self):
        return sum(one_animal.space_required
                   for one_animal in self.animals)

    def __repr__(self):
        output = f"Cage {self.id_number}\n"
        output += '\n'.join('\t' + str(animal)
                            for animal in self.animals)
        return output

class BigCage(Cage):
    pass


wolf = Wolf('black')
sheep1 = Sheep('white')
sheep2 = Sheep('black')
sheep3 = Sheep('blue')
snake = Snake('brown')
parrot = Parrot('green')

c1 = Cage(1, 10)
c1.add_animals(wolf)

c2 = Cage(2, 20)
c2.add_animals(snake, parrot)

bc = BigCage(3, 30)
bc.add_animals(wolf, sheep1, sheep2, sheep3, snake)

bc2 = BigCage(4, 50)
bc2.add_animals(wolf, sheep1, sheep2, sheep3, snake, parrot)

print(c1)
print(c2)
print(bc)
print(bc2) 
