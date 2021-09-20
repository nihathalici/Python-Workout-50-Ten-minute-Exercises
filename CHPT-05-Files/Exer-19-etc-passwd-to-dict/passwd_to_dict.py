
def passwd_to_dict(fname):
    return {
        one_line.split(':')[0] : int(one_line.split(':')[2])
        for one_line in open(fname)
        if not one_line.startswith(('#', '\n'))
    }

print(passwd_to_dict('passwd.txt'))
                                     
