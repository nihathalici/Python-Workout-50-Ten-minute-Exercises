
'''
Combine the animals_by_color and animals_by_legs methods into a single
get_animals method, which uses kwargs to get names and values. The only
valid names would be color and legs. The method would then use one or both
of these keywords to assemble a query that returns those animals that match
the passed criteria.
'''

class Animal():
    pass

class Wolf(Animal):
    pass

class Sheep(Animal):
    pass

class Snake(Animal):
    pass

class Parrot(Animal):
    pass

class Cage:
    pass

class NoColorsPassedError(Exception):
    pass

class Zoo:
    pass
