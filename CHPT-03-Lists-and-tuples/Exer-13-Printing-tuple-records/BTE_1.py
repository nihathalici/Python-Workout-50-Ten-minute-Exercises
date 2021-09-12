'''
If you find tuples annoying because they use numeric indexes, you’re not alone! Reimplement this exercise 
using namedtuple objects (http://mng.bz/gyWl), defined in the collections module. Many people like to use 
named tuples because they give the right balance between readability and efficiency.
'''

import collections
from operator import itemgetter

PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]


def sort_using_ntuple(iter):

    st = ''
    person = collections.namedtuple('person',('firstname','lastname','hours'))
    persons = [person(p[0],p[1],p[-1]) for p in iter]
    for item in sorted(persons, key=lambda x: (x.lastname,x.firstname)):
        st += f'{item.lastname:<10} {item.firstname:<10} {item.hours:>5.2f}\n'
    return st

print(sort_using_ntuple(PEOPLE))
