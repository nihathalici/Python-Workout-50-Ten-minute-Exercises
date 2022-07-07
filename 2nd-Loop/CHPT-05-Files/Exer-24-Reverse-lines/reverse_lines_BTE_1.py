
'''
“Encrypt” a text file by turning all of its characters into their numeric
equivalents (with the built-in ord function) and writing that file to disk.
Now “decrypt” the file (using the built-in chr function), turning the numbers
back into their original characters.
'''

def crypt(inp_data='data.txt', encr_fl='encr.txt', decr_fl='decr.txt'):
    with open(inp_data) as rd, open(encr_fl, 'w') as encr:
        for l in rd:
            for c in l:
                encr.write(f' {ord(c)} ') if ord(c) != 10 else encr.write(f'{ord(c)}\n')
                
    with open(encr_fl, 'r') as encr, open(decr_fl, 'w') as decr:
        for l in encr:
            for c in l.rstrip('\n').split():
                decr.write(chr(int(c)))

crypt()
