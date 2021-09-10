
'''
Instead of finding the word with the greatest number of repeated letters,
find the word with the greatest number of repeated vowels.
'''

from collections import Counter

WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']

def vow_word(wo):
    vwl = ('a', 'e', 'i', 'o', 'u')
    c = Counter(wo)
    return max([c[v] for v in vwl]) 


def most_rep_vwl(wos):
    return max(wos,key=vow_word)

print(most_rep_vwl(WORDS))
