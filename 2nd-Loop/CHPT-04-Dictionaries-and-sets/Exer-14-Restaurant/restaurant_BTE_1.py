'''
Create a dict in which the keys are usernames and the values are passwords,
both represented as strings. Create a tiny login system, in which the user
must enter a username and password. If there is a match, then indicate
that the user has successfully logged in. If not, then refuse them entry.
(Note: This is a nice little exercise, but please never store unencrypted
passwords. It’s a major security risk.)'''


USERS = {'user1':'password1','user2':'password2', 'user3':'password3'}

def pass_check():
    name_input = input('Your username: ').strip().lower()
    pass_input= input('Now your password: ').strip().lower()
    if name_input in USERS.keys():
        if pass_input == USERS[name_input]:
            print('You are successfully logged in')
        else:
            print('Password is not correct!')
    else:
        print('Please try again')

pass_check()

    
