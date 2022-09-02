from getpass import getpass

users = [
    ('Rolf', 'idkps'),
    ('Jose', 'baby1234'),
    ('Bob', 'hacker1976'),
    ('Kenny', 'boy98')
]

username_mapping = {
    username: (idx, username, password)
    for idx, (username, password) in enumerate(users)
}

# print(username_mapping.get('Bob'))
username_input = input('Enter your username: ')
password_input = getpass('Enter your password: ')

if username_input in username_mapping \
    and username_mapping[username_input][2] == password_input:
    print("Login successfully.")
else:
    print('Login failed, please try again!')
