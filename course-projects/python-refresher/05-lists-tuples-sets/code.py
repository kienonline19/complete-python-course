friends = ['Bob', 'Anne', 'Jenny']
print(type(friends))
print(friends[0])  # Bob
print(friends[-1])  # Jenny

friends[0] = 'Smith'
print(friends)

friends.append('Jack')
print(friends)

friends.remove('Anne')
print(friends)

friends = ('Bob', 'Anne', 'Jenny')
print(type(friends))

# TypeError
# friends[0] = 'Smith'

friends = {'Bob', 'Anne', 'Jenny'}
print(type(friends))

friends.add('Bob')
friends.add('Bob')
friends.add('Bob')
friends.add('Bob')
print(friends)

# TypeError
# print(friends[-1])
