# def greet():
#     print("hello")


# hello = greet
# hello()

operations = {
    'average': lambda seq: sum(seq) / len(seq),
    'total': sum,
    'top': max
}


students = [
    {"name": "Roft", "grades": (56, 67, 78, 89)},
    {"name": "Jen", "grades": (89, 100, 45, 56)},
    {"name": "Anne", "grades": (61, 73, 98, 78)},
    {"name": "Kenny", "grades": (72, 83, 92, 99)}
]

for student in students:
    name = student['name']
    grades = student['grades']

    print(f"Student: {name}")

    operation = input("Enter: 'average', 'total' or 'top': ")
    print(operations[operation](grades))
