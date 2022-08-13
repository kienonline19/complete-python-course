class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
        
    def average(self):
        return sum(self.marks) / len(self.marks)
    
    
rolf = Student('Rolf', 'MIT')

rolf.marks.append(78)
rolf.marks.append(99)

print(rolf.average())
# print(Student.average(rolf))
# print(Student.average("hello"))

class Foo:
    @classmethod
    def hi(cls):
        print(cls)
        print(cls.__name__)
        
        
Foo.hi()
my_object = Foo()
my_object.hi()

class Bar:
    @staticmethod
    def hi():
        print('Hello, I don\'t take parameters!')
        
        
Bar.hi()
Bar().hi()
