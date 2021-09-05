
'''
Write a function that takes a list or tuple of numbers. Return a two-element list,
containing (respectively) the sum of the even-indexed numbers and the sum of the odd-indexed numbers.
So calling the function as even_odd_sums([10, 20, 30, 40, 50, 60]), you’ll get back [90, 120].

Alternative Solution-II:
'''


def even_odd_sums(seq):

    sum_even = sum(seq[0::2])
    sum_odd  = sum(seq[1::2])
    return [sum_even, sum_odd]

print(even_odd_sums([10, 20, 30, 40, 50, 60]))
