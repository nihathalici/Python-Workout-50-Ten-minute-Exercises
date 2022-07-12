
'''
Write a function, transform_lines, that takes three arguments: a function
that takes a single argument, the name of an input file, and the name of
an output file. Calling the function will run the function on each line
of the input file, with the results written to the output file.

(Hint: the previous exercise and this one are closely related.)
'''

def transform_lines(fun, f_in, f_out):
    with open(f_in) as f_rd, open(f_out, 'w') as f_wr:
        for l in f_rd:
            f_wr.write(fun(l))

transform_lines( (lambda x: x.lower()), 'sonnet_126.txt', 'output_2.txt')

