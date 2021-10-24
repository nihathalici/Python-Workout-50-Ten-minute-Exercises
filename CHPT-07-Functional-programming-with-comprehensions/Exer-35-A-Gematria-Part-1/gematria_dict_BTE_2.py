
'''
Create a dict based on the config file, as in the previous exercise, but this time, all of the
values should be integers. This means that you’ll need to filter out (and ignore) those values
that can’t be turned into integers.
'''

def crt_dct_int(a_file):
    return { l.split('=')[0].strip():int(l.split('=')[-1].strip())
             for l in open(a_file)
             if l.split('=')[-1].strip().isdigit()
             }

print(crt_dct_int('config.txt'))


