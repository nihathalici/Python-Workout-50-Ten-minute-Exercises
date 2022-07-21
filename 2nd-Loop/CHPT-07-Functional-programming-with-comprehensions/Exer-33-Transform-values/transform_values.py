
d = {'a':1, 'b':2, 'c':3}

def transform_values(func, a_dict):
    return {key : func(value)
            for key, value in a_dict.items()}

def square(x):
    return x ** 2

print(transform_values(square, d))
