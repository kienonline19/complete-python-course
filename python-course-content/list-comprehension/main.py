numbers = [0, 1, 2, 3, 4]
numbers = range(5)

# doubled_numbers = []

# for number in numbers:
#     doubled_numbers.append(number * 2)

# print(doubled_numbers)

# print(number)

doubled_numbers = [number * 2 for number in numbers]
# print(number) - NameError
print(doubled_numbers)

print([5 for _ in range(5)])

friend_ages = [22, 31, 35, 37]
age_strings = [f"My friend is {age} years old." for age in friend_ages]

print(age_strings)

names = ['Roft', 'Bob', 'Jen']

lowers = [name.lower() for name in names]
print(lowers)

friend = input("Enter your friend name: ")
friends = ["Roft", "Bob", "Jen", "Jack", "Charlie", "Anne"]

friends_lower = [friend.lower() for friend in friends]

if friend.lower() in friends_lower:
    print(f"{friend.title()} is one of your friends.")

