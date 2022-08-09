"""
my_student = {
    'name': 'Roft Smith',
    'grades': [70, 88, 90, 99, 100],
    'average': ... # something that calculates average e.g: 86.75 -> 90 (add 100)
}


def average_grade(student):
    grades = student['grades']
    return sum(grades) / len(grades)


print(average_grade(my_student))
"""
class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)


# create a new object of type Student
student_one = Student('Roft Smith', [70, 88, 90, 99, 100])
print(student_one.name)
print(student_one.__class__)

student_two = Student("Jose", [78, 89, 99, 100])
print(student_two.name)
