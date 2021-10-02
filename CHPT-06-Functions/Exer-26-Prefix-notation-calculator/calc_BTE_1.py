'''
Expand the program you wrote, such that the user’s input can contain any number of numbers,
not just two. The program will thus handle
+ 3 5 7
or
/ 100 5 5,
and will apply the operator from left to right—giving the answers 15 and 4, respectively.
'''
import operator
import functools

def redu_fun(fu, nums):
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        it_obj = iter(nums)
        res = next(it_obj)
        for item in it_obj:
            res = fu(res, item)
    return res

def calc_ext(inp_str):
    op_di = {'+': operator.add, '-': operator.sub, '**': operator.pow,
             '/': operator.floordiv, '%': operator.mod, '*': operator.mul}
    op, *nums = inp_str.split()
    nums = [int(n) for n in nums]
    
    return redu_fun(op_di[op],nums)


print(calc_ext('+ 3 5 7'))
print(calc_ext('/ 100 5 5'))
