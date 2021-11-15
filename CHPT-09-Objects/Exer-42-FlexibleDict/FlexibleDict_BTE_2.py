'''
The RecentDict class works just like a dict, except that it contains a user-defined
number of key-value pairs, which are determined when the instance is created. In a
RecentDict(5), only the five most recent key-value pairs are kept; if there are more
than five pairs, then the oldest key is removed, along with its value.

Note: your implementation could take into account the fact that modern dicts store
their key-value pairs in chronological order.
'''

class RecentDict(dict):
    def __init__(self, maxsize):
        super().__init__()
        self.maxsize = maxsize

    def __setitem__(self, key, value):
        dict.__setitem__(self, str(key), value)

        if len(self) > self.maxsize:
            self.pop(list(self.keys())[0])


rd = RecentDict(5)

rd[1] = 100

rd[2] = 200

rd[3] = 300

rd[4] = 400

rd[5] = 500

rd[6] = 600

print(rd)  # prints {'2': 200, '3': 300, '4': 400, '5': 500, '6': 600}




        


