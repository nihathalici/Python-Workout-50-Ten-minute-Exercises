'''
Write a function, apply_to_each, that takes two arguments: a function that takes a single argument,
and an iterable. Return a list whose values are the result of applying the function to each element
in the iterable. 
'''

def apply_to_each(fun, my_iter):
    return [fun(item) for item in my_iter] 

print(apply_to_each( (lambda x: x * 2), [4, 5, 6] ))
