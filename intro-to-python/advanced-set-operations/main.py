''' Advanced Set Operations '''
art_friends = {"Roft", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

art_but_not_science = art_friends.difference(science_friends)
print(art_but_not_science) # {'Anne', 'Roft'}

science_but_not_art = science_friends.difference(art_friends)
print(science_but_not_art) # {"Charlie"}

not_in_both = art_friends.symmetric_difference(science_friends)

# {"Roft", "Charlie", "Anne"}
print(not_in_both)

not_in_both = science_friends.symmetric_difference(art_friends)

# {"Roft", "Charlie", "Anne"}
print(not_in_both)

# {"Jen"}
art_and_science = art_friends.intersection(science_friends)
print(art_and_science)

# {'Jen', 'Charlie', 'Anne', 'Roft'}
all_friends = art_friends.union(science_friends)
print(all_friends)
