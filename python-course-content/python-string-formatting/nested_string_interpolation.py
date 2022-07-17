name = 'Jose'
print(f'Hello, {name}') # Hello, Jose

print('Hello, {}'.format(name)) # Hello, Jose

print('---------------------------------------------')

number_of_files = 3
number_digits = 1

"""
image001.png
image002.png
image003.png
"""

for file_number in range(1, number_of_files + 1):
    print(f'image{file_number:0{number_digits}}.png')
    number_digits += 1

number_of_files = 4
number_digits = int(input("> "))

for file_number in range(1, number_of_files + 1):
    print(
        'image{number:0{padding_number}}.jpg'.format(
            number=file_number,
            padding_number=number_digits
        )
    )
