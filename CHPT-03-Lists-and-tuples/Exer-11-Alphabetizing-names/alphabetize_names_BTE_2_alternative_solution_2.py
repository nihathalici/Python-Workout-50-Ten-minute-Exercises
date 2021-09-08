'''
Given a list of strings, sort them according to how many vowels they contain.
'''

def vowel_cnt(word):
    cnt = 0
    for ch in word.lower():
        if ch in 'aeiou':
            cnt += 1
    return cnt


def vowel_sort(iter):
    return sorted(iter, key=vowel_cnt)


str_lst = ['eyewitness', 'Robot', 'abbreviation']

print(vowel_sort(str_lst))

