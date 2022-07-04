"""
String Formatting
"""

age = 34
age_as_str = str(age)

print("You are " + age_as_str)
print(f'You are {age}')

name = 'Jose'
greeting = f'How are you, {name}?'

print(greeting)
name = 'Bob'
print(greeting)

final_greeting = 'How are you, {}?'
bob_greeting = final_greeting.format(name)
print(bob_greeting)

john_greeting = final_greeting.format('John')
print(john_greeting)

friend_name = 'Jerry'
final_greeting = 'How are you, {name}?'
print(final_greeting.format(name=friend_name))

template = "{} is {age} years old!"
print(template.format('Bob', age=30))
