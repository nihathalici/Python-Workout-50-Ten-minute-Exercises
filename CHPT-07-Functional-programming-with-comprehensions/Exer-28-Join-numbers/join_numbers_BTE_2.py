
'''
Given a list of strings containing hexadecimal numbers, sum the numbers together.
'''

def hex_sum(hex_lst):
    return sum(int(x, base=16) for x in hex_lst)

print(hex_sum([hex(4), hex(9), hex(-4), hex(11)]))
