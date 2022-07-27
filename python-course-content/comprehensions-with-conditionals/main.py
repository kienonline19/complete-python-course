ages = [22, 35, 27, 21, 20]

odds = [age for age in ages if age % 2 != 0]
print(odds)

print("---------------------------------------------")

friends = ["Roft", "ruth", "charlie", "Jen"]
guests = ['jose', "Bob", "Roft", "Charlie", "michael"]

# guests_lower = {g.lower() for g in guests}
# friends_lower = {f.lower() for f in friends}

# print({friend.title() for friend in guests_lower.intersection(friends_lower)})

friends_lower = [f.lower() for f in friends]

present_friends = [
    name.title()
    for name in guests
    if name.lower() in [f.lower() for f in friends]
]

print(present_friends)
