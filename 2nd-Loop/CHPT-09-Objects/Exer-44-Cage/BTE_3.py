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

animal_safety = {Wolf: [Wolf, Snake, Parrot],
                 Sheep: [Sheep, Snake, Parrot],
                 Snake: [Wolf, Sheep],
                 Parrot: [Wolf, Sheep]}

class DangerousAssignmentError(Exception):
    pass

class Cage():
    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []
    
    def add_animals(self, *animals):
        for one_animal in animals:
            for one_current_resident in self.animals:
                if type(one_animal) not in animal_safety[type(one_current_resident)]:
                    raise DangerousAssignmentError(
                        f'You cannot put a {type(one_animal)} with a {type(one_current_resident)}!')
            self.animals.append(one_animal)
    
    def __repr__(self):
        output = f'Cage {self.id_number}\n'
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

c1 = Cage(1)
c1.add_animals(wolf)

c2 = Cage(2)
c2.add_animals(snake, sheep1)

bc = BigCage(3)
bc.add_animals(wolf, sheep1, sheep2, sheep3, snake)

bc2 = BigCage(4)
bc2.add_animals(wolf, sheep1, sheep2, sheep3, snake, parrot)

print(c1)
print(c2)
print(bc)
print(bc2)
