'''
Write a function that takes a list of dicts and returns a single dict that combines
all of the keys and values. If a key appears in more than one argument, the value should
be a list containing all of the values from the arguments.
'''
"""
def sum_dict(li_dict):
    fin_dict = {}
    for item in li_dict:
        for k in item:
            if k in fin_dict:
                fin_dict[k] = list(fin_dict[k]) + [item[k]]
            else:
                fin_dict[k] = item[k]
    return fin_dict
"""

def sum_dict(li_dict):
    fin_dict = {}
    for item in li_dict:
        for k in item:
            if k in fin_dict:
                fin_dict[k] = list(fin_dict[k]) + [item[k]]
            else:
                fin_dict[k] = item[k]
    return fin_dict


print(sum_dict([ {1: 'a', 2: 'b'}, {1: 'c', 3: 'd'}, {1: 'a', 2: 'b', 4: 'f'} ]))
