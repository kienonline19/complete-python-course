"""
def add(x, y=3):
    total = x + y
    return total

# def sub(x=3, y):
#     return x - y


print(add(5, 10)) # 15
print(add(5)) # 8
print(add(5, 1)) # 6
print(add(x=3)) # 6
print(add(x=5, y=2)) # 7
# print(add(x=5, 2)) # SyntaxError
print(add(5, y=100))
# print(add(y=10)) # TypeError

# print(sub(1, 100)) # SyntaxError

print(1, 2, 3, 4, sep=' - ')
"""
default_y = 23


def add(x, y = default_y):
    total = x + y
    return total


print(add(12)) # 35
default_y = 4

print(add(12)) # 35
