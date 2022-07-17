"""
friend_name = "Roft"
user_name = input("Enter your name: ")

if user_name == friend_name:
    print("Hello, friend!")
    print("This runs too.")
# if user_name != friend_name:
# print("Hello") - Error
else:
    print("Hello, stranger!")

print("This runs anyway.")
    # print("Hello") - Error

print(bool(5)) # True
print(bool(0)) # False

if 5:
    print("Runs.")
name = input("Enter your name: ")
print(bool(name))

if name:
    print("We know your name.")
"""
friends = ["Roft", "Bob", "Anne"]
family = ["Jen", "Charlie"]

user_name = input("Enter your name: ")

if user_name in friends:
    print("Hello, friend!")
elif user_name in family:
    print("Hello, family!")
else:
    print("I don't know you.")












