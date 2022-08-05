'''
With FlexibleDict, we allowed the user to use any key, but were then
flexible with the retrieval. Implement StringKeyDict, which converts
its keys into strings as part of the assignment. Thus, immediately
after saying skd[1] = 10, you would be able to then say skd['1'] and
get the value of 10 returned. This can come in handy if you’ll be reading
keys from a file and won’t be able to distinguish between strings and integers.
'''

class StringKeyDict(dict):
    def __setitem__(self, key, value):
        dict.__setitem__(self, str(key), value)

skd = StringKeyDict()

skd[1] = 10
print(skd['1'])
print(type(skd.keys()))

