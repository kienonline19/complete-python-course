''' Tuples In Python '''
short_tuple = "Roft", "Bob"

print(type(short_tuple))
print(short_tuple)

a_bit_clearer = ('Roft', 'Bob')

print(type(a_bit_clearer))
print(a_bit_clearer)

tuple_in_list = [('Roft', 'Bob')]
print(tuple_in_list)

not_a_tuple = 'Roft',

print(type(not_a_tuple))
print(not_a_tuple)

friends = ('Roft', 'Bob', 'Anne')
print(id(friends))
# friends.append('Jen')

# friends += 'Jen',
friends += ('Jen',)
print(id(friends))

print(friends)

print('----------------------------------------------')

lst = [1, 2, 3]
lst[0] = 2
print(lst)

tup = 1, 2, 3
print(tup[0])

# tup[0] = 3 - TypeError
x = 'x',

