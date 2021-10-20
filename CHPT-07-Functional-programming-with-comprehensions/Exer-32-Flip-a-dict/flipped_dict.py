
my_dict = {'a':1, 'b':2, 'c':3, 'd':3}

def flipped_dict(a_dict):
    return {
        value : key
        for key, value in a_dict.items()
    }

print(flipped_dict(my_dict))

