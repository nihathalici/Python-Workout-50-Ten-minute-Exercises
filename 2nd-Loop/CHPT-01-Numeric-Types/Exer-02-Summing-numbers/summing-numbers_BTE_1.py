"""
The built-in version of sum takes an optional second argument, which is used as
the starting point for the summing. (That’s why it takes a list of numbers as its
first argument, unlike our mysum implementation.) So sum([1,2,3], 4) returns
10, because 1+2+3 is 6, which would be added to the starting value of 4. Reimplement
your mysum function such that it works in this way. If a second argument
is not provided, then it should default to 0. Note that while you can write
a function in Python 3 that defines a parameter after *args , I’d suggest avoiding
it and just taking two arguments—a list and an optional starting point.
"""

def mysum(li, num=0):
    output = 0
    for item in li:
        output += item
    return output + num

print(mysum([1, 2, 3], 4))
