"""
# def divide(x, y):
#     return x / y


divide = lambda x, y: x / y
# print(divide(1, 0)) # Error
print(divide(1, 2)) # 0.5


print((lambda x, y: x + y)(3, 4)) # 7
"""


# def average(seq):
#     return sum(seq) / len(seq)


average = lambda seq: sum(seq) / len(seq)


students = [
    {'name': 'Roft', 'grades': (90, 87, 75, 78)},
    {'name': 'Bob', 'grades': (64, 73, 82, 91)},
    {'name': 'Jen', 'grades': (56, 78, 89, 99)},
    {'name': 'John', 'grades': (76, 85, 80, 100)}
]

for student in students:
    print(average(student['grades']))


add = lambda x, y: x + y
print(add)

print(add(1, 2))
