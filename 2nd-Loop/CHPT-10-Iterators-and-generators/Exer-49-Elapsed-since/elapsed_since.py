'''
A generator that takes an iterable as input.

With each iteration, it yields a tuple containing the data and the time
since the previous iteration.
'''
import time
import random

def elapsed_since(data):
    last_time = None
    for one_item in data:
        current_time = time.perf_counter()
        delta = current_time - (last_time or current_time)
        last_time = time.perf_counter()
        yield (delta, one_item)

for t in elapsed_since('abcd'):
    time.sleep(random.randint(0, 2))
    print(t)
