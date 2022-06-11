'''
Given a sequence of positive and negative numbers, sort them by absolute value.
'''

def sorting_numbers(iter):
    return sorted(iter, key=abs)

print(sorting_numbers([7, 15, 20, 1]))

