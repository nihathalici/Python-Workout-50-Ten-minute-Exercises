'''
Reading from that same server log, what response codes were returned to users?
The 200 code represents “OK,” but there are also 403, 404, and 500 errors.
(Regular expressions aren’t required here but will probably help.)
'''

def log_chq_2(fname):
    
    er_set = set()

    with open(fname,'r') as f:
        for l in f:
            er_set.add(l.split(' ')[8])
    return er_set

    
print(log_chq_2('log_file.txt'))
