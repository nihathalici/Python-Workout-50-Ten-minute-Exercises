'''
The existing function elapsed_since reported how much time passed between
iterations. Now write a generator function that takes two arguments
—a piece of data and a minimum amount of time that must elapse between
iterations. If the next element is requested via the iterator protocol
(i.e., next), and the time elapsed since the previous iteration is
greater than the user-defined minimum, then the value is returned.
If not, then the generator uses time.sleep to wait until the appropriate
amount of time has elapsed.
'''

import time
import random

def elapsed_since(data, min_wait):
    last_time = None
    for item in data:
        current_time = time.perf_counter()
        delta = current_time - (last_time or current_time)

        if delta < min_wait:
            time.sleep(min_wait - delta)

        last_time = time.perf_counter()
        yield (delta, item)

for t in elapsed_since('abcd', 0.5):
    time.sleep(random.randint(0, 2))
    print(t)
