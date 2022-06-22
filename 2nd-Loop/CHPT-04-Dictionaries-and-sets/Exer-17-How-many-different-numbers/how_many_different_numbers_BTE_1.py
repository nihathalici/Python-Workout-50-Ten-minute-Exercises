
'''
Read through a server (e.g., Apache or nginx) log file. What were the different
IP addresses that tried to access your server?
'''

def log_chq(fname):
    ip_s = set()
    with open(fname, 'r') as f:
        for l in f:
            ip_s.add(l.partition(' ')[0])
    return ip_s

print(log_chq('log_file.txt'))
