# def hello():
#     print('Hello world!')


# hello()

"""
def user_age_in_seconds():
    user_age = int(input('enter your age: '))
    age_seconds = user_age * 365 * 24 * 60 * 60

    print(f'Your age in seconds is {age_seconds}.')


print('Welcome to the age in seconds program!')
user_age_in_seconds()

print('Goodbye!')
"""

# DON'T USE
def print():
    print('Hello')


print()

# SHADOWING A VARIABLE
friends = ['Rolf', 'Jack', 'Kenny', 'Bob']


def add_friend():
    global friends
    friend_name = input('Enter your friend name: ')
    friends = friends + [friend_name]


print(friends)
add_friend()
print(friends)

# say_hello()


# def say_hello():
#     print('Hello!')

# def add_friend():
#     friends.append('Rolf')


# friends = []
# add_friend()

# print(friends) # ['Rolf']

# BEST PRACTICE
# friends = []


# def add_friend():
#     friends.append('Rolf')


# add_friend()
# add_friend()
# add_friend()
# add_friend()
# add_friend()

# print(friends)  # ['Rolf']
