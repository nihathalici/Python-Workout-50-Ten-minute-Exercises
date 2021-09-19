'''
Read through a text file, line by line. Use a dict to keep track of how many times
each vowel (a, e, i, o, and u) appears in the file. Print the resulting tabulation.
'''

def vwl_cnt(fname):
    vwl_di = {'a': 0, 'e':0, 'i':0, 'o':0, 'u':0}
    with open(fname) as f:
        c = ' '
        while c:
            c = f.read(1)
            if not (c in vwl_di):
                continue
            vwl_di[c] += 1
    for x, y in vwl_di.items():
        print(x, y)


print(vwl_cnt('sonnet_126.txt'))


