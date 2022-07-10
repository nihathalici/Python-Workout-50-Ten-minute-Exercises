'''
Write a “factorial” function that takes any number of numeric arguments and
returns the result of multiplying them all by one another.
'''

def fact_fun(*args):
    if len(args) == 1:
        return args[0]
    return args[0] * fact_fun(*args[1:])

print(fact_fun(2))
print(fact_fun(2, 3, 4))

