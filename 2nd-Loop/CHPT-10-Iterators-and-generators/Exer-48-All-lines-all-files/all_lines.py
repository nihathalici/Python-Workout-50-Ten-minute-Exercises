'''
Write an iterator (as a generator function) that returns each line
from each file in a named directory.

Any file that cannot be opened, for whatever reason, is ignored.
'''
import os
def all_lines(path):
    for filename in os.listdir(path):
        full_filename = os.path.join(path, filename)
        try:
            for line in open(full_filename):
                yield line
        except OSError:
            pass

for one_line in all_lines('Files'):
    print(one_line)
