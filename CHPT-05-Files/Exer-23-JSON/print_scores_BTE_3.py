"""
Ask the user for the name of a directory. Iterate through each file in that directory
(ignoring subdirectories), getting (via os.stat) the size of the file and when it was
last modified. Create a JSON-formatted file on disk listing each filename, size, and
modification timestamp. Then read the file back in, and identify which files were
modified most and least recently, and which files are largest and smallest, in that
directory.
"""

import csv, json, pathlib, time

def rd_dir(dname='.'):
    fl_inf = {}
    for el in pathlib.Path(dname).iterdir():
        if el.is_dir():
            continue
        fl_inf[el.name] = [el.stat().st_size, el.stat().st_mtime]
    with open('fl_info.json','w') as out:
        json.dump(fl_inf, out, indent=4)
    with open('fl_info.json') as rd:

        val = json.load(rd)
        sz_srt = sorted(val, key=lambda x: val[x][0])
        dt_srt = sorted(val, key=lambda x: val[x][1])
        print(f'Most recently modified: {dt_srt[-1]}: {time.ctime(val[dt_srt[-1]][1])}')
        print(f'Least recently modified: {dt_srt[0]}: {time.ctime(val[dt_srt[0]][1])}')
        print(f'Largest: {sz_srt[-1]}: {val[sz_srt[-1]][0]/1000:.2f} KB')
        print(f'Smallest: {sz_srt[0]}: {val[sz_srt[0]][0]/1000:.2f} KB')


rd_dir()
