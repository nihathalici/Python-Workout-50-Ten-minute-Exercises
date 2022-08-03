'''
Python provides a __del__ method that’s executed when an object is garbage collected.
(In my experience, deleting a variable or assigning it to another object triggers the
calling of __del__ pretty quickly.) Modify your Person class such that when a Person
instance is deleted, the population count decrements by 1.

If you aren’t sure what garbage collection is, or how it works in Python, take a look
at this article: http://mng.bz/nP2a.
'''

class Person:
    population = 0
    def __init__(self, name):
        self.name = name
        Person.population += 1

    def __del__(self):
        Person.population -= 1

p1 = Person('James')
p2 = Person('John')
p3 = Person('Robert')
#p4 = Person('Michael')
#p5 = Person('William')

print(Person.population)  # prints only 3
        
