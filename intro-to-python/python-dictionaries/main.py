''' Python Dictionaries '''
friend_ages = {
    "Roft": 24,
    "Adam": 30,
    "Anne": 27,
    "Adam": 100
}

print(friend_ages["Roft"])

# friend_ages["Bob": 20]
friend_ages["Bob"] = 20
friend_ages["Roft"] = 25

print(friend_ages)

friends = (
    {"name": "Roft", "age": 20},
    {"name": "Adam", "age": 34},
    {"name": "Anne", "age": 30}
)

friends[0]["name"] = "Roft Smith"
print(friends[0]["name"]) # Roft Smith
print(friends[1]["name"]) # Adam
print(friends[2]["name"]) # Anne

friends = [("Roft", 24), ("Adam", 30), ("Anne", 27)]
friends_dict = dict(friends)

print(friends_dict)

friends = [["Roft", 24], ["Adam", 30], ["Anne", 27]]
friends_dict = dict(friends)

print(friends_dict)
