'''
Ask the user to enter integers, separated by spaces. From this input, create a dict
whose keys are the factors for each number, and the values are lists containing those
of the users’ integers that are multiples of those factors.
'''

def get_factor(num):
    return { x for x in range(1, num + 1) if not num % x }

def factor_chq():
    nums = input('> ').split()
    nums = [int(num) for num in nums if num.isdigit()]
    d_keys = list(map(get_factor, nums))
    s_keys = set()
    for n in d_keys:
        s_keys.update(n)
    d_keys = { k:[k*v for v in nums] for k in s_keys }
    print(d_keys)

factor_chq()
