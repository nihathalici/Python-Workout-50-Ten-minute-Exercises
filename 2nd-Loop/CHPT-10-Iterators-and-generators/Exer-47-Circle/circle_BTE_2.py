
'''
Implement Circle as a generator function, rather than as a class.
'''

def circle(data, max_times):
    for index in range(max_times):
        yield data[index % len(data)]

c = circle("abcd", 7)

print('** A **')
for one_item in c:
    print(one_item)

print('** B **')
for one_item in c:
    print(one_item)