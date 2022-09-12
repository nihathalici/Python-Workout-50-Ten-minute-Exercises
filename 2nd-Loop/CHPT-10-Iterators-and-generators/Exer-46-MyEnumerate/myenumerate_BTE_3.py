
'''
Redefine MyEnumerate as a generator function, rather than as a class.
'''

def my_enumerate(data, start=0):
    index = start

    for one_item in data:
        yield (index, one_item)
        index += 1

print(my_enumerate('abcd'))
print(*my_enumerate('abcd', 1))