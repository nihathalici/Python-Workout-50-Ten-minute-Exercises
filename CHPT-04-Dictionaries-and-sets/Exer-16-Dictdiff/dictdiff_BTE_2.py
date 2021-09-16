
'''
Write a function that takes any even number of arguments and returns a dict
based on them. The even-indexed arguments become the dict keys, while the odd-
numbered arguments become the dict values. Thus, calling the function with the
arguments ('a', 1, 'b', 2) will result in the dict {'a':1, 'b':2} being returned.
'''

def even_ind_di(*elem):
    return {k:v for k,v in zip(elem[::2], elem[1::2])}

print(even_ind_di('0', 1, '2', 3, 'a', 4, '5', 'b', '6', 7, 'c'))
