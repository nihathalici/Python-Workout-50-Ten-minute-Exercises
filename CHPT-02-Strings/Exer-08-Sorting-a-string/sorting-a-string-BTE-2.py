
"""
Which is the longest word in a text file?
"""

def find_longest(fname):
    lo_wo = ''
    with open(fname,'r') as f:
        for li in f:
            t = ''
            for c in li:
                if c.isalnum() or c ==' ': t += c
            lgt = sorted(t.split(), key=len)[-1]
            if len(lo_wo) <  len(lgt): lo_wo = lgt
    return lo_wo, len(lo_wo)

print(find_longest('my_text.txt'))

