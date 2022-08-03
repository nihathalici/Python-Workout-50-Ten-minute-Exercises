
'''
Define a Person class, and a population class attribute that increases each time
you create a new instance of Person. Double-check that after you’ve created five
instances, named p1 through p5, Person.population and p1.population are both equal to 5.
'''

class Person:
    population = 0
    def __init__(self, name):
        self.name = name
        Person.population += 1

p1 = Person('James')
p2 = Person('John')
p3 = Person('Robert')
p4 = Person('Michael')
p5 = Person('William')

print(Person.population)
