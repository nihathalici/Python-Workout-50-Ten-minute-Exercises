
'''
Turn menu.py into a Python package and upload it to PyPI. (I suggest using
your name or initials, followed by “menu,” to avoid name collisions.) See
the sidebar on the difference between modules and packages, and how you can
participate in the PyPI ecosystem with your own open-source projects.
'''

def menu(**options):
    while True:
        option_string = '/'.join(sorted(options))
        choice = input(f'Enter an option ({option_string}): ')
        if choice in options:
            return options[choice]()
        print('Not a valid option')
