
'''
Find a configuration file in which the lines look like "name=value."
Use a dict comprehension to read from the file, turning each line
into a key-value pair.
'''


def di_frm_fl(fname):
    with open(fname) as f:
        return {l.split(':')[0]:l.split(':')[1] for l in f}

print(di_frm_fl('my_data_dir/config_file'))
