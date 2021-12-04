'''
Modify all_lines such that it doesn’t return a string with each iteration,
but rather a tuple. The tuple should contain four elements: the name of the file,
the current number of the file (from all those returned by os.listdir), the
line number within the current file, and the current line.
'''

import os

def all_lines_tuple(path):
    for file_index, filename in enumerate(os.listdir(path)):
        full_filename = os.path.join(path, filename)
        try:
            for line_index, line in enumerate(open(full_filename)):

                yield (full_filename, file_index, line_index, line)
        except OSError:
            pass


for one_line in all_lines_tuple('txt_files'):
    print(one_line)
