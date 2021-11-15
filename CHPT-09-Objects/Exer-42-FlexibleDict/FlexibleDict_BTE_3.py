'''
The FlatList class inherits from list and overrides the append method.
If append is passed an iterable, then it should add each element of the
iterable separately. This means that fl.append([10, 20, 30]) would not
add the list [10, 20, 30] to fl, but would rather add the individual
integers 10, 20, and 30. You might want to use the built-in iter
function (http://mng.bz/Qy2G) to determine whether the passed argument
is indeed iterable.
'''


class FlatList(list):
    def append(self, new_value):
        try:
            for one_item in new_value:
                list.append(self, one_item)
        except TypeError:
            list.append(self, new_value)


fl = FlatList([10, 20, 30])

print(fl)
