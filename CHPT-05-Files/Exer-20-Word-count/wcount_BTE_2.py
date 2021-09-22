'''
Create a dict in which the keys are the names of files on your system and the
values are the sizes of those files. To calculate the size, you can use os.stat
(http://mng.bz/dyyo).
'''

import os

def fl_sz(pth):

    fl_di = {}
    for fl in os.listdir(pth):
        fl_di[fl] = os.stat(fl).st_size
    print(fl_di)

print(fl_sz('my_directory'))
