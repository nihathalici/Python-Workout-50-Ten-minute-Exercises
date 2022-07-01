"""
Ask the user for a directory name. Show all of the files in the directory, as well
as how long ago the directory was modified. You will probably want to use a
combination of os.stat and the Arrow package on PyPI (http://mng.bz/nPPK)
to do this easily.
"""

from pathlib import Path
from datetime import datetime

def modfy_tme(path='.'):
    res_di = {}
    with Path(path) as dir:
        res_di['DIR'] = str(dir.cwd())
        res_di['DLM'] = datetime.fromtimestamp(dir.stat().st_mtime).ctime()
        for file in dir.iterdir():
            if file.is_file():
                res_di['F'] = list(res_di.get('F', [])) + [[file.name, datetime.utcfromtimestamp(file.stat().st_mtime).ctime()]]
    return res_di

print(modfy_tme())
