
'''
Redo this exercise, but replace each grandchild’s name (currently a string)
with a dict. Each dict will contain two name-value pairs, name and age. Produce
a list
of the grandchildren’s names, sorted by age, from eldest to youngest.
'''

my_fml_tr = {'A': {'B': 12, 'C': 7, 'D': 13}, 'E': {'F': 14, 'G': 1}}

def sort_by_age(fml_tr):
    grandch = {in_k:fml_tr[k][in_k]
               for k in fml_tr
               for in_k in fml_tr[k]}
    print(grandch)
    return sorted(grandch, key=lambda x: grandch[x])

print(sort_by_age(my_fml_tr))
