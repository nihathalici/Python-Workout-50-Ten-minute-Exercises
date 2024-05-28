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

* Write a function that takes a list of numbers. It should return the average (i.e., arithmetic mean) of those numbers.
```python
def mysum(li):
    output = 0
    len_li = len(li)
    for item in li:
        output += item
    avg_num = output // len_li
    return avg_num

print(mysum([10, 20, 30, 40]))
```  


* Write a function that takes a list of words (strings). It should return a tuple containing three integers,
representing the length of the shortest word, the length of the longest word, and the average word length.


```python
def word_stats(li):
    word_len = []
    for item in li:
        word_len.append((len(item), item))

    word_len.sort()

    avg_word_len = 0

    for num in word_len:
        avg_word_len += num[0]

    avg_word_len = avg_word_len // len(word_len)

    print(f"\nLongest word: {word_len[-1][1]}")
    print(f"Length of the longest word: {word_len[-1][0]}")
    print(f"\nShortest word: {word_len[0][1]}")
    print(f"Length of the shortest word: {word_len[0][0]}")
    print()
    print(f"The average word length is: ", avg_word_len)
    print()
    print(f"({word_len[0][0]}, {word_len[-1][0]}, avg_word_len)")

word_stats(["Py", "Python", "Exercises"])
```
