# Write a program to create a decorator function to measure the execution time of a function.
# Example: Function took 0.0016 seconds to execute.

import time
from functools import wraps

def measure_time(x):
    @wraps(x)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = x(*args, **kwargs)
        end = time.time()
        total = end - start
        print(f"Function took {total} seconds to execute.")
        return result
    return wrapper

@measure_time
def example_function():
    time.sleep(2)

example_function()
