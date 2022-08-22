'''
As you can see, there are no limits on how many animals can potentially be put
into a cage. Just as we put a limit of three scoops in a Bowl and five in a
BigBowl, you should similarly create Cage and BigCage classes that limit the
number of animals that can be placed there.
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
    def  __init__(self, color):
        super().__init__(color, 4)

class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)

class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)

class Cage():
    max_animals = 3

    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []
    
    def add_animals(self, *animals):
        for one_animal in animals:
            if len(self.animals) < self.max_animals:
                self.animals.append(one_animal)
    
    def __repr__(self):
        output = f"Cage {self.id_number}\n"
        output += '\n'.join('\t' + str(animal)
                             for animal in self.animals)
        return output

class BigCage(Cage):
    max_animals = 5

wolf = Wolf('black')
sheep1 = Sheep('white')
sheep2 = Sheep('black')
sheep3 = Sheep('blue')
snake = Snake('brown')
parrot = Parrot('green')

c1 = Cage(1)
c1.add_animals(wolf, sheep1, sheep2, sheep3)

c2 = Cage(2)
c2.add_animals(snake, parrot)

bc = BigCage(3)
bc.add_animals(wolf, sheep1, sheep2, sheep3, snake)

bc2 = BigCage(4)
bc2.add_animals(wolf, sheep1, sheep2, sheep3, snake, parrot)

print(c1)  # sheep3 don't print
print(c2)
print(bc)
print(bc2) # parrot don't print
