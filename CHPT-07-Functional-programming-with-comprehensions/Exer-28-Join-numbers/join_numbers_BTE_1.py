
'''
As in the exercise, take a list of integers and turn them into strings. However,
you’ll only want to produce strings for integers between 0 and 10. Doing this
will require understanding the if statement in list comprehensions as well.
'''

def int_to_str(*args):
    return [str(x) for x in args if x >= 0 and x <= 10]

print(int_to_str(*[21,2,4,9,10,33,66]))
