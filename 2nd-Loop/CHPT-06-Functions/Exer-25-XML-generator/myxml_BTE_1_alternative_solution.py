'''
Write a copyfile function that takes one mandatory argument—the name of an
input file—and any number of additional arguments: the names of files to
which the input should be copied. Calling

copyfile('myfile.txt', 'copy1.txt', 'copy2.txt', 'copy3.txt')

will create three copies of myfile.txt:
one each in copy1.txt, copy2.txt, and copy3.txt.
'''

import shutil
from pathlib import Path

def copyfile_shutil(f_in, *args):
    if not args:
        print('No file is given.\nPlease try again.')
        return
    else:
        for f in args:
            shutil.copyfile(Path(f_in), Path(f))

copyfile_shutil('sonnet_126.txt', 'copy1.txt', 'copy2.txt', 'copy3.txt', 'copy4.txt')


















