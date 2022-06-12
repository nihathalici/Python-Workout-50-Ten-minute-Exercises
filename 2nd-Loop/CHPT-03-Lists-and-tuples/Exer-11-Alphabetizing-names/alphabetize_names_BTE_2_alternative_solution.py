'''
Given a list of strings, sort them according to how many vowels they contain.
'''

def vowel_sort(iter):

    return sorted(  iter, key=lambda x: x.count('a') + x.count('e') + x.count('u') +
                                                       x.count('i') + x.count('o'))
    

str_lst = ['eyewitness', 'Robot', 'abbreviation']

print(vowel_sort(str_lst))


