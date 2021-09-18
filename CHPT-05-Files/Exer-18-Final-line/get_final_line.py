
# Given a filename, return the final line in that file.

def get_final_line(fname):
    fin_li = ''
    for cur_li in open(fname):
        fin_li = cur_li
    return fin_li

print(get_final_line('sonnet_126.txt'))
