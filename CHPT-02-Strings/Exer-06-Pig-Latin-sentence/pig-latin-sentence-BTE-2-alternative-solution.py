
'''
Write a function that transposes a list of strings, in which each string contains
multiple words separated by whitespace. Specifically, it should perform in such a way
that if you were to pass the list ['abc def ghi', 'jkl mno pqr', 'stu vwx yz'] to the function,
it would return ['abc jkl stu', 'def mno vwx', 'ghi pqr yz'].
'''

old_list = ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']

def func(old_list):
    new_list = []
    sentence = ''.join(old_list)
    index_one = sentence[0:3] + ' ' + sentence[11:14] + ' ' + sentence[22:25]
    index_two = sentence[4:7] + ' ' + sentence[15:18] + ' ' + sentence[26:29]
    index_three = sentence[8:11] + ' ' + sentence[19:22] + ' ' + sentence[30:32]
    new_list.append(index_one)
    new_list.append(index_two)
    new_list.append(index_three)
    return new_list

print(func(old_list))    
