
'''
Given an existing text file, create two new text files. The new files will each contain
the same number of lines as the input file. In one output file, you’ll write all of the
vowels (a, e, i, o, and u) from the input file. In the other, you’ll write all of the
consonants. (You can ignore punctuation and whitespace.)
'''


def en_de_crypt(f_in='data_vwl.txt', f_vow='vwls.txt', f_con='cons.txt'):

    all_vwl = 'aeiou'
    with open(f_in) as rd_f, open(f_vow, 'w') as vwl_f, open(f_con, 'w') as con_f:
        for l in rd_f:
            for c in l:
                if c in all_vwl:
                    vwl_f.write(c)
                elif c.isalpha() and not(c in all_vwl):
                    con_f.write(c)
            else:
                vwl_f.write('\n')
                con_f.write('\n')



en_de_crypt()
