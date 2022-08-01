friends = ['Roft', 'John', 'Jack']

# counter = 0

# for friend in friends:
#     print(counter, friend)
#     counter += 1

for counter, friend in enumerate(friends, start=1):
    print(counter, friend)

print(list(enumerate(friends)))

print(list(zip(range(3), friends)))
print(dict(enumerate(friends)))
