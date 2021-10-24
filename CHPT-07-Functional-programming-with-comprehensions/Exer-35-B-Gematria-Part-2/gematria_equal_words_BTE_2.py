'''
Create a list of tuples in which each tuple contains three elements: (1) the author’s
first and last names, (2) the book’s title, and (3) the book’s price in U.S. dollars.

Use a dict comprehension to turn this into a dict whose keys are the book’s titles,
with the values being another (sub-) dict, with keys for (a) the author’s first name,
(b) the author’s last name, and (c) the book’s price in U.S. dollars.
'''

tpl_lst = [ ('Isaac Asimov','Foundation', 9), ('Frank Herbert','Dune', 12), (' George Orwell', 'Nineteen Eighty-Four', 15) ]


def tpl_li_dct():
    return {tt:{nm:pr}
            for nm, tt, pr in tpl_lst}

print(tpl_li_dct())
