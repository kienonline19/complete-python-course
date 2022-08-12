class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super(WorkingStudent, self).__init__(name, school)
        self.salary = salary
        
    def weekly_salary(self):
        return self.salary * 37.5


rolf = WorkingStudent('Rolf', 'MIT', 15.50)
print(rolf.salary)

rolf.marks.extend([45, 56, 78, 89])
print(rolf.average())

print(rolf.weekly_salary())
anna = Student('Anna', 'Oxford')
