
'''
Write a function that partly emulates the built-in zip function (http://mng.bz/ Jyzv),
taking any number of iterables and returning a list of tuples. Each tuple will contain
one element from each of the iterables passed to the function. Thus, if I call
myzip([10, 20,30], 'abc'), the result will be [(10, 'a'), (20, 'b'), (30, 'c')]. You can return
a list (not an iterator) and can assume that all of the iterables are of the same length.
'''

def myzip(iterable):
    new_iter = [[(elem[x]) for elem in iterable] for x in range(len(iterable[0]))]
    return [tuple(elem) for elem in new_iter]


print(myzip([[10, 20,30], 'abc']))
