'''
Write a function that takes a list or tuple of numbers. Return the result of alternately adding and subtracting numbers
from each other. So calling the function as plus_minus([10, 20, 30, 40, 50, 60]),
you’ll get back the result of 10+20-30+40-50+60, or 50.

Alternative solution:
'''

def plus_minus(seq):

    return seq[0] + sum(seq[1::2]) - sum(seq[2::2])


print(plus_minus([10, 20, 30, 40, 50, 60]))
