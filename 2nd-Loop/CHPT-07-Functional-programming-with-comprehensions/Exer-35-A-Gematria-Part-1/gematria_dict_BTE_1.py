
'''
Many programs’ functionality is modified via configuration files, which are often set using
name-value pairs. That is, each line of the file contains text in the form of name=value,
where the = sign separates the name from the value. I’ve prepared one such sample config file
at http://mng.bz/rryD. Download this file, and then use a dict comprehension to read its contents
from disk, turning it into a dict describing a user’s preferences. Note that all of the values
will be strings.
'''

def crt_dct(a_file):
    return { l.split('=')[0].strip():l.split('=')[-1].strip()
             for l in open(a_file)
             }

print(crt_dct('config.txt'))

###

def crt_dct(a_file):
    return {l.split('=')[0].strip():l.split('=')[-1].strip()
            for l in open(a_file)
        }

print(crt_dct('config.txt'))

