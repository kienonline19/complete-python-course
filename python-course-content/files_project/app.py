my_file = open('data.txt', mode='r')
file_content = my_file.read()
my_file.close()

print(file_content)

user_name = input('enter your name: ')
my_file_writing = open('data.txt', 'w')
my_file_writing.write(f'Hello, {user_name}!')

my_file_writing.close()
