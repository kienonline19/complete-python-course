friends = ["Roft", "Jen", "Anne"]

for friend in friends:
    print(friend)

elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for index in elements:
    print(index)

for _ in range(10):
    print("Hello world!")

for num in range(5, 10):
    print(num, end=' ')

print()
for num in range(2, 20, 3):
    print(num, end=' ')

print('#######################################################')

students = [
    {"name": "Roft", "grade": 89},
    {"name": "Jen", "grade": 97},
    {"name": "Kenny", "grade": 85},
    {"name": "Jack", "grade": 90},
    {"name": "Bob", "grade": 100}
]

for student in students:
    name = student['name']
    grade = student['grade']
    print(f"{name} has a grade of {grade}")
