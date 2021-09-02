
'''
Write a function that transposes a list of strings, in which each string contains
multiple words separated by whitespace. Specifically, it should perform in such a way
that if you were to pass the list ['abc def ghi', 'jkl mno pqr', 'stu vwx yz'] to the function,
it would return ['abc jkl stu', 'def mno vwx', 'ghi pqr yz'].
'''

old_list = ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']

lists = [x.split() for x in old_list]

print([" ".join(x) for x in zip(*lists)])

