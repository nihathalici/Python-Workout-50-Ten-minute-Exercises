'''
Write a generator function, file_usage_timing, that takes a single directory
name as an argument. With each iteration, we get a tuple containing not just
the current filename, but also the three reports that we can get about a file’s
most recent usage: its access time (atime), modification time (mtime), and
creation time (ctime).

Hint: all are available via the os.stat function.
'''

import os

def file_usage_timing(dirname):
    for one_filename in os.listdir(dirname):
        full_filename = os.path.join(dirname, one_filename)

        yield(full_filename,
          os.stat(full_filename).st_mtime,
          os.stat(full_filename).st_ctime,
          os.stat(full_filename).st_atime)
    
for item in file_usage_timing('txt_files'):
    print(item)

