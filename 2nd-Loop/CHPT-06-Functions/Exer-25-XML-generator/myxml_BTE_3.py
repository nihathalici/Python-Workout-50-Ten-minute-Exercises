'''
Write an anyjoin function that works similarly to str.join, except that the first
argument is a sequence of any types (not just of strings), and the second argument
is the “glue” that we put between elements, defaulting to " " (a space).

So anyjoin([1,2,3]) will return 1 2 3,
and anyjoin('abc', pass:'**') will return pass:a**b**c.
'''

def anyjoin(iter, glue=' '):
    return glue.join([str(x) for x in iter])

print(anyjoin([1,2,3]))
print(anyjoin('abc', glue='**'))
