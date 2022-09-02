numbers = [1, 3, 5]

# doubled = []

# for num in numbers:
#     doubled.append(num * 2)

# print(doubled)

# doubled = [x*2 for x in numbers]
# print(doubled)

friends = ['Samantha', 'Saurabh', 'Sam']
starts_s = [friend for friend in friends if friend.lower().startswith('s')]

print(friends[0] is starts_s[0])
print(friends is starts_s)
print("friends:", id(friends))
print("starts_s:", id(starts_s))

print('*' * 30)
starts_s = friends

print(friends is starts_s)
print("friends:", id(friends))
print("starts_s:", id(starts_s))

