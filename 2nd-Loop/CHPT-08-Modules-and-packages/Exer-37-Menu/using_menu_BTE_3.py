
'''
Define a module stuff with three variables—a, b, and c—and two functions— foo
and bar. Define __all__ such that from stuff import * will cause a, c, and
bar to be imported, but not b and foo.
'''

from menu_BTE_3 import a, c, bar

print(a)
print(c)
print(bar())

