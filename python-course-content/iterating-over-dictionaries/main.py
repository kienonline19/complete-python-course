friend_ages = {
    "Roft": 25,
    "Charlie": 30,
    "Bob": 27,
    "Anne": 23
}

print(friend_ages['Roft']) # 25

for name in friend_ages:
    print(name)

for name, age in friend_ages.items():
    print(name, age)

for age in friend_ages.values():
    print(age)

