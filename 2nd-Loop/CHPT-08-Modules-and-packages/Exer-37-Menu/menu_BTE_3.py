
'''
Define a module stuff with three variables—a, b, and c—and two functions— foo
and bar. Define __all__ such that from stuff import * will cause a, c, and
bar to be imported, but not b and foo.
'''


__all__ = ['a', 'c', 'bar']
a = 100
b = [10, 20, 30]
c = {'a': 1, 'b': 2, 'c': 3}

def foo():
    return 'Hello from foo!'

def bar():
    return 'Hello from bar!'

