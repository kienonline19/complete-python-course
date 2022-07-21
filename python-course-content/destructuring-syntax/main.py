currencies = 0.8, 1.2

# <class 'tuple'>
# (0.8, 1.2)
print(type(currencies))
print(currencies)

# Destructuring Syntax
usd, eur = currencies

# 0.8
print(usd)

# 1.2
print(eur)

friends = [
    ("Roft", 25),
    ("Jen", 31),
    ("Charlie", 23),
    ("Bob", 45),
    ("Henry", 34)
]

"""
Roft is 25 years old.
Jen is 31 years old.
Charlie is 23 years old.
Bob is 45 years old.
Henry is 34 years old.
"""
for name, age in friends:

    # name, age = friend
    # name = friend[0]
    # age = friend[1]

    print(f"{name} is {age} years old.")
