
'''
Write a function that takes a list or tuple of numbers. Return a two-element list,
containing (respectively) the sum of the even-indexed numbers and the sum of the odd-indexed numbers.
So calling the function as even_odd_sums([10, 20, 30, 40, 50, 60]), you’ll get back [90, 120].
'''

def even_odd_sums(sequence):
    even_sum = 0
    odd_sum = 0
    for i, item in enumerate(sequence):
        if i % 2 == 0:
            even_sum += item
        else:
            odd_sum += item
    return even_sum, odd_sum

print(even_odd_sums([10, 20, 30, 40, 50, 60]))
        
    
