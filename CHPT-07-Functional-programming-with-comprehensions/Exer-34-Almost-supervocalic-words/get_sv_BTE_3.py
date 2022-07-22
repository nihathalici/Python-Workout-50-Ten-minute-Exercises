
"""
Create a list whose elements are strings—the names of people in your family.
Now use a set comprehension (and, better yet, a nested set comprehension) to
find which letters are used in your family members’ names.
"""

# Author's solution

import string

def letters_in_names(list_of_names):
    return {one_letter
            for one_letter in ''.join(list_of_names)
            if one_letter in string.ascii_letters}

my_lst_names = ['Iris', 'Angel', 'Carlos', 'Mariate', 'Miguel']
print(letters_in_names(my_lst_names))
