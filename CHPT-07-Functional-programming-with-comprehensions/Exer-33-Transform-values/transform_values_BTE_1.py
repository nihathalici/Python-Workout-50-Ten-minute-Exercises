'''
Expand the transform_values exercise, taking two function arguments, rather than just one.
The first function argument will work as before, being applied to the value and producing
output. The second function argument takes two arguments, a key and a value, and
determines whether there will be any output at all. That is, the second function will
return True or False and will allow us to selectively create a key-value pair in the output dict.
'''

def transform_values_ext(fun1, fun2, d):
    return { k:fun1(v) for k,v in d.items() if fun2(k,v) }

def square(x):
    return x ** 2

def is_odd(a, b):
    return b % 2 != 0 


d = {'a':1, 'b':2, 'c':3, 'd': 4, 'e': 5}


print(transform_values_ext(square, is_odd, d))
