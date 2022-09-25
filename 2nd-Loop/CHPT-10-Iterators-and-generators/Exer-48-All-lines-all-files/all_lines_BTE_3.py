
'''
Modify all_lines such that it takes two arguments—a directory name, and a string.
Only those lines containing the string (i.e., for which you can say s in line) should
be returned. If you know how to work with regular expressions and Python’s re module,
then you could even make the match conditional on a regular expression.
'''

import os

def all_lines(path, s):
    for filename in os.listdir(path):
        full_filename = os.path.join(path, filename)
        try:
            for line in open(full_filename, encoding="utf-8"):
                if s in line:
                    yield line
        except OSError:
            pass

for one_line in all_lines('txt_files', 'Python'):
    print(one_line)
