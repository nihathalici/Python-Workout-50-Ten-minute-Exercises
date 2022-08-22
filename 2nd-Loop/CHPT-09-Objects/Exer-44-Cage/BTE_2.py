'''
It’s not very realistic to say that we would limit the number of animals in
a cage. Rather, it makes more sense to describe how much space each animal
needs and to ensure that the total amount of space needed per animal isn’t
greater than the space in each cage. You should thus modify each of the
Animal subclasses to include a space_required attribute. Then modify the
Cage and BigCage classes to reflect how much space each one has. Adding
more animals than the cage can contain should raise an exception.
'''
class Animal:
    pass

class Wolf:
    pass

class Sheep:
    pass

class Snake:
    pass

class Parrot:
    pass

class NotEnoughSpaceError(Exception):
    pass

class Cage:
    pass

class BigCage:
    pass

