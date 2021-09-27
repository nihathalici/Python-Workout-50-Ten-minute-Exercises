
"""
Convert /etc/passwd from a CSV-style file into a JSON-formatted file. The
JSON file will contain the equivalent of a list of Python tuples, with each tuple
representing one line from the file.
"""

import csv
import json

def csv_json(fname):
    di_tp = {}
    cnt = 0

    with open(fname) as csv_rd, open('outfl_di.json', 'w') as outfl_json:
        for l in csv.reader(csv_rd, delimiter=":"):
            if not l[0].startswith("#"):
                di_tp[cnt] = l
                cnt += 1
        json.dump(di_tp, outfl_json, indent=4)


csv_json('linux-etc-passwd.txt')
