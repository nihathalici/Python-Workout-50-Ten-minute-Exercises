'''
Write a function that takes a list of dicts and returns a single dict that combines
all of the keys and values. If a key appears in more than one argument, the value should
be a list containing all of the values from the arguments.
'''

def sum_dict(li_dict):
    fin_dict = {}
    for d in li_dict:
        for i in d.keys():
            if i not in fin_dict.keys():
                fin_dict[i] = d[i]
            else:
                tmp_li = []
                tmp_li.append(fin_dict[i])
                tmp_li.append(d[i])
                fin_dict[i] = tmp_li
    return fin_dict


print(sum_dict([ {1: 'a', 2: 'b'}, {1: 'c', 3: 'd'}, {1: 'a', 2: 'b', 4: 'f'} ]))
print(sum_dict([{1:"one", 2: "two"}, {"three": 3, "four": 4, 1: "zero"}, {"four": 450}]))

