
"""
For a slightly different challenge, turn each line in the file into a Python dict.
This will require identifying each field with a unique column or key name. If you’re
not sure what each field in /etc/passwd does, you can give it an arbitrary name.
"""

import csv
import json

def csv_di_json(fname):
    di_tp = {}
    cnt = 0
    with open(fname) as csv_rd, open('outfl_di_2.json', 'w') as outfl_json:
        for l in csv.reader(csv_rd, delimiter=':'):
            if not l[0].startswith('#'):
                di_tp[cnt] = { i:v for i, v in enumerate(l)}
                cnt += 1
        json.dump(di_tp, outfl_json, indent=4)


csv_di_json('linux-etc-passwd.txt')
