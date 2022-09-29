"""
import time


def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()
    print(f'{end - start}s')


def powers(limit):
    return [x**2 for x in range(limit)]


measure_runtime(lambda: powers(5000000))
"""

import timeit

print(timeit.timeit("[x**2 for x in range(100)]"))
print(timeit.timeit("list(map(lambda x: x**2, range(100)))"))
