
mylist = [10, 20, 30]

def join_numbers(numbers):
    return ','.join(str(x) for x in numbers)

print(join_numbers(mylist))
