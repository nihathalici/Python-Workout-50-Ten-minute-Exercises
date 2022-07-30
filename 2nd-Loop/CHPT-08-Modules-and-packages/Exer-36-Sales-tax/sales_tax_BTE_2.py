
'''
Write a module providing a function that, given a string, returns a dict
indicating how many characters provide a True result to each of the following
functions: str.isdigit, str.isalpha, and str.isspace.
The keys should be isdigit, isalpha, and isspace.
'''

def analyze_string(s):
    output = {'isdigit': 0,
              'isalpha': 0,
              'isspace': 0}

    for one_character in s:
        for methodname in output:
            if getattr(one_character, methodname)():
                output[methodname] += 1
    return output

print(analyze_string('root:*:0:0::0:0:System Administrator:/var/root:/bin/sh'))
