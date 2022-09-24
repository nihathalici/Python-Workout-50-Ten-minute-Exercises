'''
The current version of all_lines returns all of the lines from the first file,
then all of the lines from the second file, and so forth. Modify the function
such that it returns the first line from each file, and then the second line
from each file, until all lines from all files are returned. When you finish
printing lines from shorter files, ignore those files while continuing to
display lines from the longer files.
'''

import os

def open_file_safely(filename):
    try:
        return open(filename)
    except OSError:
        return None

def all_lines_alt(path):
    all_files = [open_file_safely(os.path.join(path, filename))
                 for filename in os.listdir(path)]
    
    while all_files:
        for one_file in all_files:
            if one_file is None:
                all_files.remove(one_file)
                continue

            one_line = one_file.readline()

            if one_line:
                yield one_line
            else:
                all_files.remove(one_file)

for one_line in all_lines_alt('txt_files'):
    print(one_line)


