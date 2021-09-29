
'''
The final field in /etc/passwd is the shell, the Unix command interpreter that’s
invoked when a user logs in. Create a file, containing one line per shell, in
which the shell’s name is written, followed by all of the usernames
that use the shell; for example
/bin/bash:root, jci, user, reuven, atara
/bin/sh:spamd, gitlab
'''

def rd_shll(f_in='linux-etc-passwd.txt', f_out='output.txt'):
    shll_usr = {}
    with open(f_in) as f_rd, open(f_out, 'w') as f_wr:
        for l in f_rd:
            if not l.startswith('#'):
                l = l.rstrip().split(':')
                shll_usr[l[-1]] = shll_usr.get(l[-1],[]) + [l[0]]
        for k in shll_usr:
            f_wr.write(f'{k}: {",".join(shll_usr[k])}\n')
    

rd_shll()
