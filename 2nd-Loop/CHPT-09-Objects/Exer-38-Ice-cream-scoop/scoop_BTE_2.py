
'''
Modify the Beverage class, such that you can create a new instance specifying the name,
and not the temperature. If you do this, then the temperature should have a default value
of 75 degrees Celsius. Create several beverages and double-check that the temperature has
this default when not specified.
'''

class Beverage():
    def __init__(self, name, temp=75):
        self.name = name
        self.temp = temp

b1 = Beverage('coffee', 90)
b2 = Beverage('ice tea', 5)
b3 = Beverage('water')

for item in [b1, b2, b3]:
    print('The beverage {} is {}.'.format(item.name, item.temp))
        


