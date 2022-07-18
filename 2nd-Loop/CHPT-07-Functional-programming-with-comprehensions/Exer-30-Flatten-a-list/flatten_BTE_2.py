
'''
Define a dict that represents the children and grandchildren in a family.
(See figure 7.1 for a graphic representation.) Each key will be a child’s name,
and each value will be a list of strings representing their children
(i.e., the family’s grandchildren). Thus the dict
{'A':['B', 'C', 'D'], 'E':['F', 'G']} means
that A and E are siblings; A’s children are B, C, and D;
and E’s children are F and
G. Use a list comprehension to create a list
of the grandchildren’s names.
'''

my_fml_tr = { 'A': ['B','C','D'], 'E': ['F','G']}

def fml_di(fml_tr):
    return [item
            for k in fml_tr
            for item in fml_tr[k]]

print( fml_di(my_fml_tr) )

        
