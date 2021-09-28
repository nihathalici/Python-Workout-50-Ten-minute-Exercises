
def reverse_lines(infname, outfname):
    with open(infname) as inf, open(outfname, 'w') as outf:
        for one_line in inf:
            outf.write(f'{one_line.rstrip()[::-1]}\n')


reverse_lines('input_text.txt', 'output_text.txt')
