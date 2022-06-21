
'''
Write a function , dict_partition, that takes one dict (d) and a function (f) as arguments.
dict_partition will return two dicts, each containing key-value pairs from d.
The decision regarding where to put each of the key-value pairs will be made according to
the output from f, which will be run on each key- value pair in d. If f returns True,
then the key-value pair will be put in the first output dict. If f returns False, then
the key-value pair will be put in the second output dict.
'''



d3 = {'a':1, 'b':0, 'd':3, 'e': 4}

def dict_partition(di, fn):
    f_di, s_di = {}, {}
    for k, v in di.items():
        if fn(k, v):
            f_di[k] = v
        else:
            s_di[k] = v
    return f_di, s_di

def even_chq(x, y):
    return y % 2 == 0

print(dict_partition(d3, even_chq))
