'''
Given a list of lists, with each list containing zero or more numbers,
sort by thesum of each inner list’s numbers.
'''

my_list = [[0, 1, 2], [3, 4], []]


def sort_lst(iter):
    return sorted(iter, key=sum)

print(sort_lst(my_list))

    
