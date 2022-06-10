
'''
Write a function, mysum_bigger_than, that works the same as mysum, except that it takes a first
argument that precedes *args. That argument indicates the threshold for including an argument
in the sum. Thus, calling mysum_bigger_than(10, 5, 20, 30, 6) would return 50
— because 5 and 6 aren’t greater than 10. This function should similarly work with
any type and assumes that all of the args are of the same type. Note that > and < work
on many different types in Python, not just on numbers; with strings, lists, and tuples,
it refers to their sort order.
'''

def mysum_bigger_than(*args):
    if not args:
        return args
    sum_elem = args[0]
    for i in args[1:]:
        if i < args[0]:
            pass
        else:
            sum_elem += i

    if type(sum_elem) == str:
        sum_elem = sum_elem[1:]
    elif type(sum_elem) == int:
        sum_elem = sum_elem - args[0]
    return sum_elem

print(mysum_bigger_than())
print(mysum_bigger_than(10, 5, 20, 30, 6))
print(mysum_bigger_than('i','j','a','b','z'))
