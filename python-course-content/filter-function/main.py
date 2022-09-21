def starts_with_r(friend: str) -> bool:
    return friend.startswith('R')


friends = ['Rolf', 'Jose', 'Randy', 'Jack', 'John', 'David']

"""
filter function:
arg1 - function that return True/False
arg2 - iterable: list, tuple, dict, set, zip, 
filter, enumerate, map, strings ...
return: generator
"""
# filter object (iterator and iterable)
start_with_r = filter(starts_with_r, friends)

# print(next(start_with_r))
# print(next(start_with_r))
# print(next(start_with_r))

# print(list(start_with_r))
# print(list(start_with_r))

start_with_r = filter(lambda x: x.startswith('R'), friends)
print(list(start_with_r))

# generator expression: better and faster
another_starts_with_r = (friend for friend in friends if friend.startswith('R'))
print(list(another_starts_with_r))

# custom filter function
def custom_filter_func(func, iterable):
    for i in iterable:
        if func(i):
            yield i

gen = custom_filter_func(lambda x: x.startswith('R'), friends)
print(next(gen))
print(next(gen))
print(next(gen))
