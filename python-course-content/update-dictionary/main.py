# update: allow us to extend a dict with {key: value} pairs
student = {
    "name": "John",
    "age": 28,
    "maths": "A*"
}

student_copy = student.copy()
student_copy1 = student.copy()

grades = {
    "english": "A",
    "science": "A*",
    "maths": "B"
}

student.update(grades)

print(student)

print("----------------------------------------------------------------\
----------------")

grades = [
    ("english", "A"),
    ("science", "A*"),
    ("maths", "B"),
]

student_copy.update(grades)

print(student_copy)

print("----------------------------------------------------------------\
----------------")

student_copy1.update(english='A', maths='B', science='A*')
print(student_copy1)
