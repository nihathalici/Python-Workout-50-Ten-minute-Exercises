
"""
Which is the last word, alphabetically, in a text file?
"""
def find_last(fname):
    la_wo = ''
    with open(fname, 'r') as f:
        for l in f:
            t = ''
            for c in l:
                if c.isalnum() or c == ' ':
                    t += c
            final = sorted(t.split())[-1]
            if la_wo < final:
                la_wo = final

    return la_wo


print(find_last('my_text.txt'))

