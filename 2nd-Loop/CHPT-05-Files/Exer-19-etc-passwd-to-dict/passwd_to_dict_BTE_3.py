'''
From /etc/passwd, create a dict in which the keys are the usernames (as in the main exercise)
and the values are themselves dicts with keys (and appropriate values) for user ID, home directory, and shell.
'''

def passwd_dict(filename):
    new_dict, inner_dict = {}, {}
    with open(filename) as file:
        for line in file:
            if line.startswith(('#','_','\n')):
                continue
            line = line.replace('\n', '').split(':')
            new_dict[line[0]] = {'User ID': line[2], 'home directory': line[8], 'shell': line[-1]}
    return new_dict

def passwd_di_2(fname):
    out_d, in_d = {}, {}
    with open(fname) as f:
        for l in f:
            if l.startswith(('#', '_', '\n')):
                continue
            l = l.replace('\n', '').split(':')
            out_d[l[0]] = {'user id': l[2], 'home dir': l[8], 'shell': l[-1]}
    return out_d

print(passwd_di_2('passwd.txt'))
        


