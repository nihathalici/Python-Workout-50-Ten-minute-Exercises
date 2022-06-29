'''
Create a dict in which the keys are the names of files on your system and the
values are the sizes of those files. To calculate the size, you can use os.stat
(http://mng.bz/dyyo).
'''

from pathlib import Path

def fl_sz(pth):
    fl_di = {}
    for fl in Path(pth).iterdir():
        if fl.is_dir():
            continue
        fl_di[fl.name] = fl.stat().st_size
    print(fl_di)

fl_sz('my_directory')



