'''
Open a log file from a Unix/Linux system—for example, one from the Apache
server. For each response code (i.e., three-digit code indicating the HTTP
request’s success or failure), store a list of IP addresses that generated
that code.
'''

def log_chq(fname):

    rsp_code = {}
    with open(fname, 'r') as f:
        for l in f:
            l = l.split()
            print(l)
            rsp_code[l[8]] = rsp_code.get(l[8], []) + l[:1]
    return rsp_code

print(log_chq('log_file.txt'))
