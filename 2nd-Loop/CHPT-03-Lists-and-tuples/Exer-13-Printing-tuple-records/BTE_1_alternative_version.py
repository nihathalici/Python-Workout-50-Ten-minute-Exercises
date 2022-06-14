
import collections
from operator import itemgetter

PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

def format_sort_records(iter):
    output = []
    template = '{1:10} {0:10} {2:5.2f}'

    person = collections.namedtuple('person', ('firstname', 'lastname', 'hours'))
    persons = [person(p[0],p[1],p[-1]) for p in iter]

    for one_person in sorted(persons, key=itemgetter(1, 0)):
        output.append(template.format(*one_person))

    return output

print('\n'.join(format_sort_records(PEOPLE)))


