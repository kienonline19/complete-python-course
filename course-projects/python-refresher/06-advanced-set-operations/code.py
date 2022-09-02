friends = {'Bob', 'John', 'Anne'}
abroad = {'Bob', 'Anne'}

local_friends = {'John'}
print(type(local_friends))

local_friends = friends.difference(abroad)
print(local_friends)

print(abroad.difference(friends))  # empty set

my_var = ()
print(type(my_var))  # empty tuple

total_friends = friends.union(abroad)

print(total_friends)

print('-' * 20)

art = {'Bob', 'Jen', 'Rolf', 'Charlie'}
science = {'Bob', 'Jen', 'Adam', 'Anne'}

art_and_science = art.intersection(science)

print(art_and_science)

print(art.symmetric_difference(science))
