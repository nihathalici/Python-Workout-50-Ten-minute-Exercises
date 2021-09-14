'''
Create a dict in which the keys are usernames and the values are passwords,
both represented as strings. Create a tiny login system, in which the user
must enter a username and password. If there is a match, then indicate
that the user has successfully logged in. If not, then refuse them entry.
(Note: This is a nice little exercise, but please never store unencrypted
passwords. It’s a major security risk.)'''

USERS = {'user1':'password1','user2':'password2', 'user3':'password3'}


def pass_check():
    ch = 1
    while ch:
        name_inp = input('Your username: ')
        if not name_inp.strip():
            ch = 0
            continue
        pass_inp = input('Now your password: ')
        elem = USERS.get(name_inp, 0)
        if elem == pass_inp:
            print('You are successfully logged in')
            ch = 0
            continue
        else:
            print('Please try again')

pass_check()
            
    
