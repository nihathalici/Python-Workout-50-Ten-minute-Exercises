'''
Ask the user to enter the name of a text file and then (on one line,
separated by spaces) words whose frequencies should be counted in that file.
Count how many times those words appear in a dict, using the user-entered
words as the keys and the counts as the values.
'''

from os import path

def cnt_wrd():
    val = input('> ').split()
    fname = val[0]
    wrd_cnt_di = {k: 0 for k in val[1:]}
    with open(fname) as f:
        for l in f:
            wrds = l.strip().split()
            for wrd in wrds:
                if wrd in wrd_cnt_di:
                    wrd_cnt_di[wrd] += 1
    print(wrd_cnt_di)

cnt_wrd()
