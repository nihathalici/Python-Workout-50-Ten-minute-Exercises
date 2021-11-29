
'''
Redefine MyEnumerate as a generator function, rather than as a class.
'''

def my_enumerate(data, start=0):
    index = start

    for one_item in data:
        yield (index, one_item)
        index += 1

print(my_enumerate('abcd'))  # creates a generator object
print(*my_enumerate('abcd', 1))  # prints the tuples: (1, 'a') (2, 'b') (3, 'c') (4, 'd')
