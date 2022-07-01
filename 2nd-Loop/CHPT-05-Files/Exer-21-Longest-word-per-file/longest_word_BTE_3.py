"""
Open an HTTP server’s log file. (If you lack one, then you can read one from
me at http://mng.bz/vxxM.) Summarize how many requests resulted in numeric
response codes—202, 304, and so on.
"""

def log_chq(fname):
    cnt_di = {}
    with open(fname) as f:
        for l in f:
            l = l.split()
            cnt_di[l[8]] = cnt_di.get(l[8], 0) + 1
    return cnt_di

print(log_chq('mini-access-log.txt'))
