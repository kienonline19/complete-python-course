"""
A generator in Python is a special function
"""

# Get the entire list all at once
# def hundred_numbers():
#     i = 0
#     nums = []

#     while i < 100:
#         nums.append(i)
#         i += 1

#     return nums


# print(hundred_numbers())
# print([x * 2 for x in hundred_numbers()])

# Generator function
def hundred_numbers():
    i = 0

    while i < 100:
        yield i
        i += 1


gen = hundred_numbers()
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))

my_range_obj = range(10)
# next(my_range_obj) - TypeError
print(my_range_obj)
print(repr(my_range_obj))
print(my_range_obj.__repr__())

# Convert generator to list
print(list(gen))
