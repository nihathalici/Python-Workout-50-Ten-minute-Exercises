'''
Read through a text file, line by line. Use a dict to keep track of how many times
each vowel (a, e, i, o, and u) appears in the file. Print the resulting tabulation.
'''

from collections import Counter

def vwl_cnt(fname):
    vwl_di = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    with open(fname) as f:
        for l in f:
            c = Counter(l)
            for k in vwl_di:
                vwl_di[k] += c.get(k, 0)

    for x, y in vwl_di.items():
        print(x, y)

print(vwl_cnt('sonnet_126.txt'))


