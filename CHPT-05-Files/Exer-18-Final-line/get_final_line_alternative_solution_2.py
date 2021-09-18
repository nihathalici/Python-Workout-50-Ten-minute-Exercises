
# Given a filename, return the final line in that file.

def get_final_line(fname):
    
    with open(fname, 'r') as f:
        print(f.readlines()[-1])
        

get_final_line('sonnet_126.txt')
