'''
Explore the Decimal class (http://mng.bz/oPVr), which has an alternative floating-point
representation that’s as accurate as any decimal number can be. Write a function
that takes two strings from the user, turns them into decimal instances,
and then prints the floating-point sum of the user’s two inputs.
In other words, make it possible for the user to enter 0.1 and 0.2, and for us to get 0.3 back.
'''

def add_flo(val1, val2):
    sum_of_flo = float(val1 + val2)
    return f"{sum_of_flo:.1f}"

print(add_flo(0.1, 0.2))

