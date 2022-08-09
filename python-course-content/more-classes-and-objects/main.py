class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student_one = Student('Roft Smith', [70, 88, 90, 99, 100])
student_two = Student("Jose", [78, 89, 99, 100])

print(student_one.average())
print(student_two.average())

print(Student.average(student_one))
print(Student.average(student_two))

print('-' * 25)


def average(student):
    return sum(student.grades) / len(student.grades)


print(average(student_one))
