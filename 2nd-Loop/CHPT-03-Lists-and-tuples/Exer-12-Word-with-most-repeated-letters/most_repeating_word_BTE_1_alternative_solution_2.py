
'''
Instead of finding the word with the greatest number of repeated letters,
find the word with the greatest number of repeated vowels.
'''

from collections import Counter
import operator

WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']

def most_rep(wo):
    return operator.getitem(operator.getitem(Counter(wo).most_common(), 0), 1)

def vwl_cnt(wo):
    vwl = 'aeuio'
    filter(lambda x: x in vwl, wo)
    return most_rep(wo)

def most_repeating_vwl(wos):
    return max(wos, key=vwl_cnt)

print(most_repeating_vwl(WORDS))

