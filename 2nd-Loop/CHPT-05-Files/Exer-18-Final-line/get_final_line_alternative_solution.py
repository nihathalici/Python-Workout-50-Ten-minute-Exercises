
# Given a filename, return the final line in that file.

def get_final_line(fname):
    with open(fname, 'rb+') as f:
        f.seek(-2, 2)
        s = f.read(1)
        ch = s

        while True:
            f.seek(-2, 1)
            ch = f.read(1)
            if ch == b'\n':
                break
            s += ch

        print(str(s[::-1]), 'utf-8')

get_final_line('sonnet_126.txt')
        
