def mysum(li, num = 0):
    output = 0
    for item in li:
        output += item
    return output + num

print(mysum([1, 2, 3], 4))
