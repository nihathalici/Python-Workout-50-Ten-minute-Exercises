'''
Define a Bread class representing a loaf of bread. We should be able to invoke
a get_nutrition method on the object, passing an integer representing the number
of slices we want to eat. In return, we’ll receive a dict whose key-value pairs
will represent calories, carbohydrates, sodium, sugar, and fat, indicating
the nutritional statistics for that number of slices. Now implement two new classes
that inherit from Bread, namely WholeWheatBread and RyeBread. Each class should
implement the same get_nutrition method, but with different nutritional
information where appropriate.
'''

class Bread():
    def __init__(self):
        self.calories = 66
        self.carbs = 12
        self.sodium = 170
        self.sugar = 1
        self.fat = 0.8
    
    def get_nutrition(self, number_of_slices):
        return {key: value*number_of_slices
                for key, value in vars(self).items()}

class WholeWheatBread(Bread):
    def __init__(self):
        self.calories = 67
        self.carbs = 12
        self.sodium = 138
        self.sugar = 1.4
        self.fat = 1

class RyeBread(Bread):
    def __init__(self):
        self.calories = 67
        self.carbs = 12
        self.sodium = 172
        self.sugar = 1
        self.fat = 0.8

wheat_bread = WholeWheatBread()
print(wheat_bread.get_nutrition(3))

rye_bread = RyeBread()
print(rye_bread.get_nutrition(3))
