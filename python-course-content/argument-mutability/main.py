"""
friends_last_seen = {
    "Rolf": 30,
    "Jose": 23,
    "Anna": 19
}


def see_friend(friends, name):
    # print(id(friends))
    print(friends == friends_last_seen)
    print(friends is friends_last_seen)
    friends[name] = 0
    # use it here, some more ...


# print(id(friends_last_seen))
# print(id(friends_last_seen['Rolf']))

# see_friend(friends_last_seen, "Rolf")

# print(id(friends_last_seen['Rolf']))
# print(id(friends_last_seen))

see_friend(friends_last_seen, "Rolf")
print(friends_last_seen["Rolf"])

age = 20


def increase_age(current_age):
    print(id(current_age))
    current_age = current_age + 1


print(id(age))
increase_age(age)
print(id(age))
"""

# ids same
primes = [2, 3, 5]
print(id(primes))

# primes = primes + [7, 11] (NO NO!!!!)
# => must be primes = primes.iadd([7, 11])
# change original list
primes += [7, 11] 
print(id(primes))

list.__add__
# primes = primes.__add__([7, 11])
primes = primes + [7, 11]
print(id(primes))

primes = [2, 3, 5] + [7, 11]
print(id(primes))
