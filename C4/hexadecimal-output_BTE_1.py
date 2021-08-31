'''
Write a program that asks the user for their name and then produces a “name triangle”:
the first letter of their name, then the first two letters, then the first three,
and so forth, until the entire name is written on the final line.
'''

n = input('Your name? ')
n_l = ''
for ch in n:
    n_l += ch
    print(n_l)
