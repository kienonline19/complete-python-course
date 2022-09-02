name = 'Bob'

'''
greeting = 'Hello, {}'
print(f'Hello, {name}')

print(greeting.format(name))

name = 'Rolf'
print(greeting.format(name))
print(f'Hello, {name}')
'''

greeting = 'Hello, {}'

with_name = greeting.format(name)
print(with_name)

with_name_two = greeting.format('Rolf')
print(with_name_two)

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format('Rolf', 'Monday')

print(formatted)
