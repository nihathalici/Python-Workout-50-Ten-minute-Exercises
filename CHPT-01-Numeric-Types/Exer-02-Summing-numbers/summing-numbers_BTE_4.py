'''
Write a function that takes a list of Python objects. Sum the objects
that either are integers or can be turned into integers, ignoring the others.
'''

def sum_int(li):
    val = 0
    for item in li:
        try:
            val += int(item)
        except ValueError:
            pass
    return val

    
mylist = [1, 2, 3, 6.5, '4', 'A', 'B']

print(sum_int(mylist))
