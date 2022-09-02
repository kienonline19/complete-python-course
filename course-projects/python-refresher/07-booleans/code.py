print(5 == 5)  # Boolean comparison
print(5 > 5)
print(10 != 10)

friends = ['Rolf', 'Bob']
abroad = ['Rolf', 'Bob']

# ==
print(friends == abroad)  # True

# is
print(friends is abroad)  # False

print(friends is friends)

abroad = friends
print(friends is abroad)  # True
