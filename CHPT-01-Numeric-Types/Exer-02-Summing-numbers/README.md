```python
def mysum(*numbers):
    """Accepts any number of numeric arguments as inputs.
       Returns the sum of those numbers.
       If invoked without any arguments, returns 0.
    """
    output = 0
    for number in numbers:
        output += number
    return output

print(mysum(10, 20, 30, 40))
```

* The built-in version of sum takes an optional second argument, which is used as the starting point for the summing. (That’s why it takes a list of numbers as its first argument, unlike our mysum implementation.) So sum([1,2,3], 4) returns 10, because 1+2+3 is 6, which would be added to the starting value of 4. Reim- plement your mysum function such that it works in this way. If a second argu- ment is not provided, then it should default to 0.

```python
def mysum(li, num = 0):
    output = 0
    for item in li:
        output += item
    return output + num

print(mysum([1, 2, 3], 4))
```
