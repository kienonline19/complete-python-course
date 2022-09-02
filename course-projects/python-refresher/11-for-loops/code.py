number = 7


# while user_input != 'n':
#     user_number = int(input("Guess our number: "))

#     if user_number == number:
#         print("You guessed correctly!")
#     elif abs(number - user_number) == 1:
#         print("You were off by one.")
#     else:
#         print("Sorry, it's wrong!")

#     user_input = input("Enter 'y' if you would like to play: ").lower()

"""
while True:
    user_input = input("Enter 'y' if you would like to play: ").lower()

    if user_input == 'n':
        break

    user_number = int(input("Guess our number: "))

    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")
"""
friends = ['Rolf', 'Jen', 'Bob', 'Anne']

# for friend in friends:
#     print(f'{friend} is my friend.')

# for friend in range(4):
#     print(f'{friend} is my friend.')

grades = [35, 67, 98, 100, 100]

# total = 0
# amount = len(grades)

# for grade in grades:
#     total += grade

# print(f'{total / amount:.2f}')

print(sum(grades) / len(grades))
