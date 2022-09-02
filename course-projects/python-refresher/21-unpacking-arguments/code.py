"""
def multiply(*args):
    print(args)
    total = 1

    for arg in args:
        total *= arg
    return total


# print(multiply(1, 2, 3, 4))
print(multiply(-1))
"""

"""
def add(x, y):
    return x + y


# lst = [3, 5]
# print(add(*lst))

# print(add(y=5, x=3)) # 8
nums = {'x': 3, 'y': 5}

# print(add(nums['x'], nums['y']))
# print(add(x=nums['x'], y=nums['y']))

print(add(**nums))
"""
import math


def multiply(*args):
    return math.prod(args)


def apply(*args, operator):
    if operator == '*':
        return multiply(*args)
    elif operator == '+':
        return sum(args)
    else:
        return "No valid operator provided to apply()."


print(apply(1, 2, 5, operator='*'))
