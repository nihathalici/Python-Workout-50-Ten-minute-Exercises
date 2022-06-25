'''
Read through /etc/passwd, creating a dict in which user login shells (the final
field on each line) are the keys. Each value will be a list of the users for
whom that shell is defined as their login shell.
'''

def shell_chq(fname):
    sh_di = {}
    with open(fname) as f:
        for l in f:
            if l.startswith(('#', '\n')):
                continue
            l = l.replace('\n', '').split(':')
            sh_di[l[-1]] = list(sh_di.get(l[-1], [])) + [l[0]]

    for k, v in sh_di.items():
        print(k, ':', v)

shell_chq('passwd.txt')

