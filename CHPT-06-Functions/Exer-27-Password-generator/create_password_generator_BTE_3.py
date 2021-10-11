'''
Write a function, doboth, that takes two functions as arguments (f1 and f2)
and returns a single function, g. Invoking g(x) should return the same result
as invoking f2(f1(x)).
'''

def doboth(fun1, fun2):
    def g(x):
        return fun2(fun1(x))
    return g


f1 = lambda x: x.rstrip('\nxyz')
f2 = lambda x: x.lstrip(' 246')

strip_string_from_sides = doboth(f1,f2)

print(strip_string_from_sides(' 24444.Final String.\nzzyyx'))
print(f2(f1(' 24444.Final String.\nzzyyx')))
