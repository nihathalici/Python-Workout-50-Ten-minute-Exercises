
'''
Create a text file (using an editor, not necessarily Python) containing two
tab-separated columns, with each column containing a number. Then use Python
to read through the file you’ve created. For each line, multiply each first
number by the second, and then sum the results from all the lines.
Ignore any line that doesn’t contain two numeric columns.
'''

def sum_numbers(fname):
    tot = 0
    with open(fname) as f:
        for l in f:
            l = l.replace(' ', '')
            l = l.replace('\n', '').split(',')
            if len(l) < 2:
                continue
            if all(map(str.isdigit, l[:2])):
                print(f'{l[0]} * {l[1]} = { (int(l[0])) * (int(l[1]))}')
                tot += int(l[0]) * int(l[1])
    print(f'TOTAL: {tot}')
print(sum_numbers('num_file.txt'))
            
        
