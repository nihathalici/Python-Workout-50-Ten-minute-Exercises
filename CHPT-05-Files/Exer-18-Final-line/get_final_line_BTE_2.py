
'''
Create a text file (using an editor, not necessarily Python) containing two
tab-separated columns, with each column containing a number. Then use Python
to read through the file you’ve created. For each line, multiply each first
number by the second, and then sum the results from all the lines.
Ignore any line that doesn’t contain two numeric columns.
'''

def sum_numbers_from_file(fname):
    total = 0
    with open(fname) as f:
        for line in f:
            line = line.replace(' ', '')
            line = line.replace('\n','').split(',')
            if len(line) < 2: continue
            if all(map(str.isdigit, line[:2])):
                print(f'{line[0]} * {line[1]} = { (int(line[0])*int(line[1])) }')
                total += int(line[0]) * int(line[1])
    print(f'TOTAL: {total}')

print(sum_numbers_from_file('num_file.txt'))
