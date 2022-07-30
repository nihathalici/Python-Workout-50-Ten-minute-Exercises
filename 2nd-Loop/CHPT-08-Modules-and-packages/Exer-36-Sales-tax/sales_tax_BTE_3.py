
'''
The dict.fromkeys method (http://mng.bz/1zrV) makes it easy to create a new dict.
For example, dict.fromkeys('abc') will create the dict {'a':None, 'b':None, 'c':None}.
You can also pass a value that will be assigned to each key, as in
dict.fromkeys('abc', 5), resulting in the dict {'a':5, 'b':5, 'c':5}. Implement a function
that does the same thing as dict.keys but whose second argument is a function. The value
associated with the key will be the result of invoking f(key).
'''

def fromkeys_func(s, func):
    output = {}
    for one_item in s:
        output[one_item] = func(one_item)
    return output

