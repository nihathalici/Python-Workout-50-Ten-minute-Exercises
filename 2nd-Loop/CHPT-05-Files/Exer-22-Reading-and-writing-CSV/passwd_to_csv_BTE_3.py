'''
Create a CSV file, in which each line contains 10 random integers between 10 and 100.
Now read the file back, and print the sum and mean of the numbers on each line.
'''

import csv
from random import randint

def rndm_csv(fname):
    x, y = 7, 10
    with open(fname, 'w') as c_wr:
        wr_obj = csv.writer(c_wr)
        for row in range(x):
            wr_obj.writerow([randint(10, 100) for _ in range(y)])
    row_cnt = 0
    with open(fname, newline='\r\n') as c_rd:
        for l in csv.reader(c_rd):
            print(f'Row: {row_cnt}\t Sum: {sum([int(x) for x in l])}\t Average: {sum([int(x) for x in l]) / len(l)}')
            row_cnt += 1

rndm_csv('rndm_vl2')
        
    

















