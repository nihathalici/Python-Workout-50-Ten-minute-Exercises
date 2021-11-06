'''
Write a Beverage class whose instances will represent beverages. Each beverage
should have two attributes: a name (describing the beverage) and a temperature.

Create several beverages and check that their names and temperatures are all
handled correctly.
'''

class Beverage():
    def __init__(self, name, temp):
        self.name = name
        self.temp = temp

b1 = Beverage('coffee', 'hot')
b2 = Beverage('ice tea', 'cold')
b3 = Beverage('water', 'normal')

for item in [b1, b2, b3]:
    print('The beverage {} is {}.'.format(item.name, item.temp))
