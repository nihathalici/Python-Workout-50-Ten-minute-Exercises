'''
Given a list of strings, sort them according to how many vowels they contain.
'''

def vowel_sort(iter):
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    return sorted(iter, key=lambda x: sum([x.count(c) for c in VOWELS]))

    
str_lst = ['eyewitness', 'Robot', 'abbreviation']

print(vowel_sort(str_lst))


