print(True and True) # True
print(True and False) # False
print(True or False) # True
print(False or False) # False

print('-------------------------')

print(False and True) # False
print(True and True) # True
print(True and False) # False

print('--------------------------')
print(True or False) # True
print(False or True) # True
print(False or False) # False

print('--------------------------')
print(None and '35') # None

x = []
print(x and 12) # []
print(10 and 20) # 20

print(repr(None or '35')) # '35'
print([] or 12) # 12
print(10 or 20) # 10

print(bool(None)) # None - falsy => False
print(bool('35')) # '35' - truthy => True
print(bool(10)) # 10 - truthy => True
print(bool([])) # [] - falsy => False
print(bool([1, 2, 3])) # [1, 2, 3] - truthy => True
print(bool(0.0j))

# falsy - '', [], tuple(), {}, empty iterables
# None, 0, 0.0, 0j, 0.0j

