friends = ["Roft", "ruth", "charlie", "Jen"]
guests = ['jose', "Bob", "Roft", "Charlie", "michael"]

guests_lower = {g.lower() for g in guests}
friends_lower = {f.lower() for f in friends}

present_friends = friends_lower.intersection(guests_lower)
present_friends = {
    friend.title()
    for friend in present_friends
}

print(present_friends)

print('------------------------------------------------')

friends = ["Roft", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = {
    friend: time
    for friend, time in zip(friends, time_since_seen)
    if time > 5
}

print(long_timers)
