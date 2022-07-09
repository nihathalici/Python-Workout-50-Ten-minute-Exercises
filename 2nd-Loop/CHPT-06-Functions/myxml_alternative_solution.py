
def myxml(*args, **kwargs):
    tag, content = " ".join(args[:1]), ". ".join(args[1:])
    attr_di = [f'{k}="{v}"' for k, v in kwargs.items()]
    attr_di.insert(0, tag)
    return f'<{" ".join(attr_di)}>{content}</{tag}>'

print(myxml('foo'))
print(myxml('foo', 'text'))
print(myxml('foo', 'bar', a=1, b=2, c=3) )
