'''
In the /etc/passwd file you used earlier, what different shells (i.e., command interpreters,
named in the final field on each line) are assigned to users? Use a set comprehension to gather them.
'''

def shell_chq(sh_file):
    return { l.split(':')[-1].strip()
             for l in open(sh_file)
             if not l.startswith('#') }

print(shell_chq('user_db_with_com.txt'))

