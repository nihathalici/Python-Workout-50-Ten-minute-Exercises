#!/usr/bin/env python3

"""Function that takes keyword arguments. The value
associated with each key is a function taking zero arguments.
The user is asked to enter input.
If the input matches a keyword, then the associated function
is invoked, and its return value is returned to the user.
If the input doesn't match a keyword, the user is asked to
try again.
"""

def menu(**options):
    while True:
        option_string = '/'.join(sorted(options))
        choice = input(f'Enter an option ({option_string}): ')
        if choice in options:
            return options[choice]()
        print('Not a valid option')


