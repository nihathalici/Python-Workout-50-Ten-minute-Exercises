
'''
Create a dict whose keys are filenames and whose values are the lengths of the
files. The input can be a list of files from os.listdir (http://mng.bz/YreB)
or glob.glob (http://mng.bz/044N).
'''
"""
from pathlib import Path

def cnt_fl_di(cnt_pth):
    fl_di = {}
    my_path = Path(cnt_pth)
    fl_di = {fl.name:fl.stat().st_size for fl in my_path.iterdir() if fl.is_file()}
    return fl_di

print(cnt_fl_di('my_data_dir'))
"""

import stylecloud

stylecloud.gen_stylecloud(file_path='con.txt')
