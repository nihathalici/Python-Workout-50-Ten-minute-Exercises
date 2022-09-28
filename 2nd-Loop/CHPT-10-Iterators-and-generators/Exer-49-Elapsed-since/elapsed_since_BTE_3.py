
'''
Write a generator function that takes two elements: an iterable and
a function. With each iteration, the function is invoked on the current
element. If the result is True, then the element is returned as is.
Otherwise, the next element is tested, until the function returns True.
Alternative: implement this as a regular function that returns a generator expression.
'''

from curses.ascii import isalpha


def yield_filter(data, func):
    for one_item in data:
        if func(one_item):
            yield one_item

def is_alpha(item):
    return item.isalpha()

for item in yield_filter('+abcd23@', isalpha):
    print(item)

