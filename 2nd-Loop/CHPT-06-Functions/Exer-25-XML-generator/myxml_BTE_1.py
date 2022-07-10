'''
Write a copyfile function that takes one mandatory argument—the name of an
input file—and any number of additional arguments: the names of files to
which the input should be copied. Calling

copyfile('myfile.txt', 'copy1.txt', 'copy2.txt', 'copy3.txt')

will create three copies of myfile.txt:
one each in copy1.txt, copy2.txt, and copy3.txt.
'''

def copyfile(f_in, *args):
    if not args:
        print('No file is given.\nPlease try again.')
        return
    else:
        with open(f_in) as f_rd:
            for f in args:
                with open(f, 'w') as f_wr:
                    for l in f_rd:
                        f_wr.write(l)
                f_rd.seek(0)
                
copyfile('sonnet_126.txt', 'copy1.txt', 'copy2.txt', 'copy3.txt')
