

def myxml(tagname, content='', **kwargs):
    attributes = ''.join(f'{key}="{value}"' for key, value in kwargs.items())
    return f'<{tagname}{attributes}>{content}</{tagname}>'

print(myxml('foo'))
print(myxml('foo', 'text'))
print(myxml('foo', 'bar', a=1, b=2, c=3))


