friends = ["Roft", "Charlie", "Anna", "Bob", "Jen"]

print(friends[2:4])
print(friends[1:])
print(friends[:4])

print(id(friends))

all_friends = friends[:]
print(id(all_friends))
print(all_friends == friends)
print(friends[-3:])
print(friends[-3:4])
print(friends[:-2])
print(friends[-3:-1])
