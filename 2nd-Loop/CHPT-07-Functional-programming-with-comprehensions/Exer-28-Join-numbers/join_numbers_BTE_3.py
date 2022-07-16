
'''
Use a list comprehension to reverse the word order of lines in a text file.
That is, if the first line is
abc def
and the second line is
ghi jkl,
then you should return the list
['def abc', 'jkl ghi'].
'''

def rev_wrd_ordr(fname='text.txt'):
    res = []
    with open(fname) as f:
        res = [' '.join(line.strip().split()[::-1]) for line in f]
    return res

print(rev_wrd_ordr())
