"""
map function
arg1: function to convert
arg2: iterable
return generator
"""
friends = ['Rolf', 'Jose', 'Jen', 'David', 'Kenny', 'Danny']

friends_lower = map(str.lower, friends)
friends_lower = [friend.lower() for friend in friends]
friends_lower = (friend.lower() for friend in friends)  # best

print(next(friends_lower))


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])

    def __str__(self):
        return f"<User {self.username}, {self.password}>"


users = [
    {"username": "jose", "password": "123"},
    {"username": "tecladoisawesome", "password": "youaretoo"},
]

user_lst = [User.from_dict(user) for user in users]
print(user_lst)

user_objects = map(User.from_dict, users)

print(next(user_objects))
print(next(user_objects))
