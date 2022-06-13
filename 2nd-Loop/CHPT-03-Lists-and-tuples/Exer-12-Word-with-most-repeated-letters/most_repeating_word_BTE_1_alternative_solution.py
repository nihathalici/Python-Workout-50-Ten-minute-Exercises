
'''
Instead of finding the word with the greatest number of repeated letters,
find the word with the greatest number of repeated vowels.
'''

from collections import Counter

WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']

def vow_word(wo):
    vwl = ''
    for ch in wo.lower():
        if ch in 'aeiou':
            vwl += ch

    return Counter(vwl).most_common(1)[0][1]

def most_rep_vwl(wos):
    return max(wos, key=vow_word)

print(most_rep_vwl(WORDS))
