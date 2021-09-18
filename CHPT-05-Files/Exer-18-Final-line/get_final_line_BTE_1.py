'''
Iterate over the lines of a text file. Find all of the words (i.e., non-whitespace
surrounded by whitespace) that contain only integers, and sum them.
'''

def find_num(fname):
    with open(fname) as f:
        n_sum = 0
        for l in f:
            n_sum += sum([int(w) for w in l.split() if w.isdigit()])
    return n_sum

print(find_num('sonnet_126.txt'))


