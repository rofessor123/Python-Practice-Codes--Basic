#. Decorator - Create a decorator @time_it that measures how long a function takes to run.

#Theory: A decorator modifies function behavior without changing its code. Example: measure execution time.

import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.5f} sec")
        return result
    return wrapper

@time_it
def slow_function():
    time.sleep(2)
    print("Done!")

slow_function()