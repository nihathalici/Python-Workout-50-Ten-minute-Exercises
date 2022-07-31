
'''
Create a new LogFile class that expects to be initialized with a filename. Inside of __init__,
open the file for writing and assign it to an attribute, file, that sits on the instance.
Check that it’s possible to write to the file via the file attribute.
'''

class LogFile():
    def __init__(self, fname):
        self.file = open(fname, 'w')

f1 = LogFile('text1.txt')
f2 = LogFile('text2.txt')
f3 = LogFile('text3.txt')


