"""
x = 5
x = (5, 11)
y = 5, 11

print(x == y)
lst = [(4, 5)]

print(lst)

a, b = 1, 2
print(a)
print(b)

t = (5, 11)
x, y = t

print(x)
print(y)
"""
student_attendance = {
    'Rolf': 96,
    'Bob': 80,
    'Anne': 100
}

# for student, attendance in student_attendance.items():
#     print(f'{student}: {attendance}')

# print(list(student_attendance.items()))

# for t in student_attendance.items():
#     print(t)

people = [
    ('Bob', 42, 'Mechanic'),
    ('James', 24, 'Artist'),
    ('Harry', 32, 'Lecturer')
]

for name, age, profession in people:
    print(f'Name: {name}, Age: {age}, Profession: {profession}')

print('-' * 45)

for person in people:
    print(f'Name: {person[0]}')
    print(f'Age: {person[1]}')
    print(f'Profession: {person[2]}')

print('-' * 45)

person = ('Bob', 42, 'Mechanic')
name, _, profession = person

print(f'Name: {name}')
print(f'Profession: {profession}')

print('-' * 45)

head, *tail = [1, 2, 3, 4, 5]

print(head)
print(tail)

print('-' * 45)

*head, tail = [1, 2, 3, 4, 5]

print(*head)
print(tail)
