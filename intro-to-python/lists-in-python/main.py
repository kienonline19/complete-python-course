''' Lists In Python '''
friend1 = 'Roft'
friend2 = 'Jen'
friend3 = 'Jerry'

print(friend1)
print(friend2)
print(friend3)

friends = ['Roft', 'Jen', 'Jerry']
print(friends[0])
print(friends[1])
print(friends[-1])

print(len(friends))

friends = [['Mark', 25], ['Bob', 30], ['Anne', 27]]

friends = [
    ['Kenny', 24],
    ['Mark', 37],
    ['Bob', 46],
    ['Jen', 25],
    ['Jack', 40],
    ['John', 34]
]

print(friends[0][0])
print(friends[1][1])

friends = ['Bob', 'Jen', 'Kenny']

# friends += ['Henry']
friends.append('Henry')
print(friends)

friends.remove('Bob')
print(friends)

friends = [['Mark', 25], ['Bob', 30], ['Anne', 27]]

friends.remove(['Mark', 25])
print(friends)

# ValueError: 'Bob' not in list
# friends.remove('Bob')
