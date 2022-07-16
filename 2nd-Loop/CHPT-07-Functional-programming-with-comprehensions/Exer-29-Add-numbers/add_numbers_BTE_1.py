
'''
Show the lines of a text file that contain at least one vowel and contain
more than 20 characters.
'''

def show_lines(fname='text.txt'):
    res = []
    with open(fname) as f:
        f_lines = filter(lambda x: len(x) > 20, (li for li in f))
        for li in f_lines:
            for c in li:
                if c.lower() in 'aeiuo':
                    print(li.rstrip())
                    break

show_lines()
            
