
mylist = [[10, 20, 30], [40, 50, 60], [70, 80, 90, 100]]

def flatten(the_list):
    return [one_item
            for one_sublist in the_list
            for one_item in one_sublist]

print(flatten(mylist))
