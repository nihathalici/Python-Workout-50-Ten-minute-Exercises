import csv

def passwd_to_csv(passwd_filename, csv_filename):
    with open(passwd_filename) as passwd, open(csv_filename, 'w') as output:
        infile = csv.reader(passwd, delimiter=':')
        outfile = csv.writer(output, delimiter='\t')

        for one_record in infile:
            if len(one_record) > 1:
                outfile.writerow((one_record[0], one_record[2]))

passwd_to_csv('linux-etc-passwd.txt', 'passwd.csv')
                
