'''
Write a function that takes a list or tuple of numbers. Return the result of alternately adding and subtracting numbers
from each other. So calling the function as plus_minus([10, 20, 30, 40, 50, 60]),
you’ll get back the result of 10+20-30+40-50+60, or 50.
'''

def plus_minus(iter):
    str_acc = f'{iter[0]}'
    num_sum = iter[0]
    for i in range(1, len(iter)):
        if not (i % 2):
            str_acc += f'-{iter[i]}'
            num_sum -= iter[i]
        else:
            str_acc += f'+{iter[i]}'
            num_sum += iter[i]
    return str_acc, num_sum


print(plus_minus([10, 20, 30, 40, 50, 60]))
