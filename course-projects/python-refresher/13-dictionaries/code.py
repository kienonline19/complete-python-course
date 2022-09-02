# friend_ages = {
#     "Rolf": 24,
#     "Adam": 30,
#     "Anne": 27
# }

# friend_ages['Bob'] = 20
# print(friend_ages['Adam'])

# friend_ages['Adam'] = 34
# print(friend_ages)

# friends = [
#     {'name': 'Rolf', 'age': 24},
#     {'name': 'Bob', 'age': 27},
#     {'name': 'Anne', 'age': 30},
#     {'name': 'Adam', 'age': 28}
# ]

# print(friends[1]['name'])

student_attendance = {'Rolf': 96, 'Bob': 80, 'Anne': 100}

# for student in student_attendance:
#     print(f"{student}: {student_attendance[student]}%")

for student, attend in student_attendance.items():
    print(f'{student}: {attend}%')

name = 'Anne'

if name in student_attendance:
    # print('Bob attended this many lectures.')
    print(f"{name}: {student_attendance[name]}")
else:
    print(f'{name} is not a student in this class.')

attendance_values = student_attendance.values()
print(attendance_values)
print(sum(attendance_values) / len(attendance_values))
