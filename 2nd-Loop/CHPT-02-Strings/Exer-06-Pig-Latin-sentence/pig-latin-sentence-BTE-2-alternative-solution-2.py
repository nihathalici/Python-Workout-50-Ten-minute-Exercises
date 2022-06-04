
'''
Write a function that transposes a list of strings, in which each string contains
multiple words separated by whitespace. Specifically, it should perform in such a way
that if you were to pass the list ['abc def ghi', 'jkl mno pqr', 'stu vwx yz'] to the function,
it would return ['abc jkl stu', 'def mno vwx', 'ghi pqr yz'].
'''

from unittest import result


old_list = ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']

def li_change(li):
    new_li = []
    for i in range(len(li)):
        li[i] = li[i].split()
    for i in range(len(li)):
        new_li += [ ' '.join([nested_li[i] for nested_li in li])]
    return new_li

result = li_change(old_list)

print(result)
