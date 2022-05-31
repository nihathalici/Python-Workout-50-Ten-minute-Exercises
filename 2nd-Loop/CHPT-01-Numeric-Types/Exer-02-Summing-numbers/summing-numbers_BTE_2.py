"""
Write a function that takes a list of numbers. It should return
the average (i.e., arithmetic mean) of those numbers.
"""

def mysum(li):
    output = 0
    len_li = len(li)
    for item in li:
        output += item
    avg_num = output // len_li
    return avg_num

print(mysum([10, 20, 30, 40]))
