'''
The dict.update method merges two dicts. Write a function that takes any number
of dicts and returns a dict that reflects the combination of all of them.
If the same key appears in more than one dict, then the most recently merged
dict’s value should appear in the output.
'''

def mult_di(*args):
    fin_di = {}
    for di in args:
        fin_di.update(di)
    return fin_di


d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'd':4}
d3 = {'a':1, 'b':3, 'd':5}

print(mult_di(d1, d2, d3))
