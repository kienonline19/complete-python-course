friends_last_seen = {
    "Rolf": 31,
    "Jose": 3,
    "Anne": 45
}

print(id(friends_last_seen))

friends_last_seen = {
    "Rolf": 31,
    "Jose": 3,
    "Anne": 45
}

print(id(friends_last_seen))

friends_last_seen['Rolf'] = 0 # friends_last_seen.__setitem__(self, "Rolf", 0)

print(id(friends_last_seen))

"""
ints: all functions return new int objects
"""

my_int = 5
print(id(my_int))

my_int = my_int + 1 # my_int.__add__(1) return cls(self.value + 1) (new integer objects)
print(id(my_int))

my_int += 1 # my_int.__iadd__(self, 1)

print('-' * 20)

friends = ["Rolf", "Jose"]

print(id(friends))
friends.append("Jen")

print(id(friends))
