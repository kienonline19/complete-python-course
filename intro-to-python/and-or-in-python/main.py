''' and & or in python '''
"""
age = int(input('enter your age: '))
can_learn_programming = age > 0 and age < 150
usually_working = age >= 18 and age <= 65

print(f'You can learn programming: {can_learn_programming}.')
print(f'At {age}, you are usually working: {usually_working}.')
"""

# Falsy - 0, 0.0, '', ...
print(bool(35)) # True
print(bool('Roft')) # True
print(bool(0)) # False
print(bool('')) # False

# and: first value if it's False else second value
print(True and False) # False
print(35 and 0) # 0
print(0 and 35) # 0

# or: first value if it's True else second value
print(35 or 0) # 35
print(0 or 35) # 35

'''
name = input('enter your name: ')
surname = input('enter your surname: ')

greeting = name or f'Mr. {surname}'
print(greeting)
'''

print(not False) # True
print(not True) # False
print(not bool(35)) # False
print(not 35) # False
