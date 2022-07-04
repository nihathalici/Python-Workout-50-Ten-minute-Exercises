'''
Write a function that writes a dict to a CSV file. Each line in the CSV file
should contain three fields: (1) the key, which we’ll assume to be a string,
(2) the value, and (3) the type of the value (e.g., str or int).
'''

import csv

def csv_from_di(res_file='di_val_typ.csv'):
    di_val = {'first': '1', 'second': 2, 'three': [3, 4, '5'], 'fourth': True, 'fifth': (6, 7)}
    with open(res_file, 'w') as csv_wr:
        wr = csv.writer(csv_wr)
        for k in di_val:
            wr.writerow( [k, di_val[k], type(di_val[k]) ] )

csv_from_di()
