
'''
Use a nested list comprehension to transform a list of dicts into a list
of two- element (name-value) tuples, each of which represents one of the
name-value pairs in one of the dicts. If more than one dict has the same
name-value pair, then the tuple should appear twice.
'''


def nested_lst(di_lst):
    tpl_lst = [ (k, item[k]) for item in di_lst for k in item]
    tpl = [tpl_lst.remove(item) for item in tpl_lst if tpl_lst.count(item) > 2]
    return tpl_lst

print(nested_lst([{'a':1},{'a':1,'b':2},{'c':1,'b':2,'a':1,'d':3}]))
