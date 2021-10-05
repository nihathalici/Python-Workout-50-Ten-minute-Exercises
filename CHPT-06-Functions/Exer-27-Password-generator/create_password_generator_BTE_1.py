'''
Now that you’ve written a function to create passwords, write create_password_checker,
which checks that a given password meets the IT staff’s acceptability criteria.
In other words, create a function with four parameters: min_ uppercase,
min_lowercase, min_punctuation, and min_digits. These represent the minimum
number of uppercase letters, lowercase letters, punctuations, and digits for
an acceptable password. The output from create_password_checker is a function
that takes a potential password (string) as its input and returns a Boolean
value indicating whether the string is an acceptable password.
'''

import string

def create_password_checker(min_uppercase=0, min_lowercase=0, min_punctuation=0, min_digits=0):
    def is_valid(p_str):
        val_di = {'m_up':0,'m_low':0, 'm_dig':0, 'm_pun':0}

        for c in p_str:
            if c.isalpha() and c.islower():
                val_di['m_low'] += 1
            elif c.isalpha() and c.isupper():
                val_di['m_up'] += 1
            elif c.isdigit():
                val_di['m_dig'] += 1
            elif c in string.punctuation:
                val_di['m_pun'] += 1
        return val_di['m_low'] >= min_lowercase and val_di['m_up'] >= min_uppercase and val_di['m_dig'] >= min_digits and val_di['m_pun'] >= min_punctuation
    return is_valid


p_req_1 = create_password_checker()
p_req_2 = create_password_checker(2,4,1,2)
p_req_3 = create_password_checker(min_lowercase=14,min_punctuation=1,min_digits=3)

print(p_req_1('123456ab'))
print(p_req_2('a.s1u234D56Gl'))
print(p_req_3('as1@23hj456'))


