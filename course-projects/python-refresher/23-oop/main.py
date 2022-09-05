# student = {
#     "name": "Rolf",
#     "grades": (89, 90, 93, 78, 90)
# }


# def average(seq):
#     return sum(seq) / len(seq)


# print(average(student["grades"]))

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student_one = Student("Rolf", (89, 90, 93, 78, 90))
print(student_one.name)
print(student_one.grades)
# print(student_one.average_grade())
print(Student.average_grade(student_one))

student_two = Student('Bob', (56, 78, 90, 65, 98))
print(student_two.average_grade())
