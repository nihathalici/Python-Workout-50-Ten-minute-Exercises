'''
Generator that takes any number of iterables as arguments. It yields, one at
a time, each of the elements of each iterable.

It is similar to itertools.chain
'''

def mychain(*args):
    for one_item in args:
        for one_element in one_item:
            yield one_element

for one_item in mychain('abc', [10, 20, 30, 40, 50], (100, 200, 300), [2, 4, 6]):
    print(one_item)