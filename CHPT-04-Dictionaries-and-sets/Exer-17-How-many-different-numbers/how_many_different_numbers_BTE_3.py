'''
Use os.listdir (http://mng.bz/YreB) to get the names of files in the current directory.
What file extensions (i.e., suffixes following the final . character) appear in that directory?
It’ll probably be helpful to use os.path.splitext (http://mng.bz/GV4v).
'''

import os

def file_chq(path): 
    return set([f.partition('.')[-1] for f in os.listdir(path)])


print(file_chq('/Users/TheUser/Documents/'))

