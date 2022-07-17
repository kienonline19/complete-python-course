''' Python Strings '''
"""
Strings

This file talks about strings.
"""

my_string = 'Hello, world!'
print(my_string)
print("Hello, world!")

string_with_quotes = "Hello, it's me"
print(string_with_quotes)

another_with_quotes = 'He said: "You are amazing!" yesterday.'
print(another_with_quotes)

another_with_quotes = "He said: \"You are amazing!\" yesterday."
print(another_with_quotes)

multiline = '''Hello, world.

My name is Jose. Welcome to my program.
'''

print(multiline)

name = 'Jose'
greeting = "Hello, " + name
print(greeting)

age = 25
age_as_str = str(age)
print("You are " + age_as_str)
