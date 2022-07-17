''' Sets In Python '''
art_friends = {"Roft", "Anne"}

print(type(art_friends))
print(art_friends)

science_friends = {"Jen", "Charlie"}

print(type(science_friends))
print(science_friends)

art_friends.add("Jen")

print(art_friends)

art_friends.add("Jen")
print(art_friends)

art_friends.remove('Jen')
# art_friends.remove('Jen') - KeyError
print(art_friends)
