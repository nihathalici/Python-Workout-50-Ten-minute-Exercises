
import operator

def calc(to_solve):
    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.truediv,
                  '**': operator.pow,
                  '%': operator.mod}
    op, first_s, second_s = to_solve.split()
    first = int(first_s)
    second = int(second_s)

    return operations[op](first, second)

print(calc('+ 2 3'))

###

import operator

def calc(to_solve):
    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.truediv,
                  '**': operator.pow,
                  '%': operator.mod}
    op, first_s, second_s = to_solve.split()
    first = int(first_s)
    second = int(second_s)

    return operations[op](first, second)

print(calc('+ 2 3'))
