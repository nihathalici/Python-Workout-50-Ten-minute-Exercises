'''
Extend this exercise by asking the user to enter a space-separated list of integers,
indicating which fields should be written to the output CSV file. Also ask the user
which character should be used as a delimiter in the output file. Then read from
/etc/passwd, writing the user’s chosen fields, separated by the user’s chosen delimiter.
'''
import csv

def fnd_ln(inpfile):
    with open(inpfile) as f:
        rd = csv.reader(f, delimiter=':')
        for l in rd:
            if len(l) > 2:
                return len(l)
        return 0


def usr_csv(inpfile, outfile):
    with open(inpfile) as csv_rd, open(outfile, 'w') as csv_wr:
        rw_ln = fnd_ln(inpfile)
        fld = input('Which columns?: ')
        dlm = input('Which delimiter?: ')
        fld = list(filter(lambda x: x < rw_ln, [abs(int(x)) for x in fld.split()]))
        wr = csv.writer(csv_wr, delimiter=dlm)
        wr.writerow([f'Column numbers: {fld}'])
        rd = csv.reader(csv_rd, delimiter=':',)
        for l in rd:
            if len(l) > 1:
                wr.writerow([l[col] for col in fld])
        print('DONE')

usr_csv(inpfile='linux-etc-passwd.txt', outfile='password_out3.csv')

