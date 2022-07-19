
'''
In this exercise, plfile applied the plword function to every word in a file.
Write a new function, funcfile, that will take two arguments—a filename and
a function. The output from the function should be a string, the result of
invoking the function on each word in the text file. You can think of this
as a generic version of plfile, one that can return any string value.
'''

def plword(word):
    if word[0] in 'aeiou':
        return word + 'way'
    return word[1:] + word[0] + 'ay'

def plfile(fname):
    return ' '.join(plword(one_word)
                    for one_line in open(fname)
                    for one_word in one_line.split())

def fun_fl(fname, fun):
    return fun(fname)

print(fun_fl('sonnet_126.txt', plfile))
