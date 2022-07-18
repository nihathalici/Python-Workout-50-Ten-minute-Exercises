
'''
Write a version of the flatten function mentioned earlier called flatten_odd _ints.
It’ll do the same thing as flatten, but the output will only contain odd integers.
Inputs that are neither odd nor integers should be excluded. Inputs containing strings
that could be converted to integers should be converted; other strings should be excluded.
'''

def odd_int_fltr(the_lst):
    return [int(float(item)) \
            for sub_lst in the_lst \
            for item in sub_lst \
            if (isinstance(item, (int, float)) and item % 2) or \
            (isinstance(item, str) and (item.isdigit() or item.replace('.', '').isdigit()) \
             and float(item) % 2)]

print(odd_int_fltr( [ [7, 9, 1], {}, ['Z', 7, '8.5'] ] ))
