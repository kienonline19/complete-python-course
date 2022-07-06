''' Booleans and Comparisons '''
truthy = True
falsy = False

print(truthy, falsy)

age = 20
is_over_age = age >= 18

print(is_over_age)

is_under_age = age < 18
print(is_under_age)

is_twenty = age == 20
print(is_twenty)

print('--------------------------------')

NUMBER = 5
user_number = int(input('Enter a number: '))

matches = user_number == NUMBER
print(f'You got it right: {matches}.')
