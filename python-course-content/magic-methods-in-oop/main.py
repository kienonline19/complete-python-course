"""
class Student:
    def __init__(self, name):
        self.name = name
        
        
student_one = Student('John')
print(student_one.name)

movies = ['The Matrix', 'Finding Nemo']
print(movies.__class__)
print(type(movies))

print('hi'.__class__)

print(len(movies))
print(list.__len__(movies))
"""


class Garage:
    def __init__(self):
        self.cars = []
        
    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, i):
        return self.cars[i]
    
    # def __repr__(self):
    #     return f'<Garage {self.cars}>'

    def __repr__(self):
        return f'Garage with {len(self)} cars.'

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')
print(ford.cars)

print(len(ford))
# print('__len__' in dir(list))

print(ford[0])
print(Garage.__getitem__(ford, 0))

for car in ford:
    print(car)
    
print('-' * 20)
print(ford)
