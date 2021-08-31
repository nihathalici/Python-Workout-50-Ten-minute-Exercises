def mysum(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output

print(mysum(10, 20, 30, 40))
