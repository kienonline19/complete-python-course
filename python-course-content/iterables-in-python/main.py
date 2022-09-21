class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return self


g = FirstHundredGenerator()

print(g)
print(next(g))
print(next(g))
print(next(g))


class FirstHundredIterable:
    def __iter__(self):
        return FirstHundredGenerator()


gen = FirstHundredGenerator()

for k in gen:
    print(k)

print(sum(FirstHundredGenerator()))


# iterable = FirstHundredIterable()

# for x in iterable:
#     print(x)

# print(sum(iterable))

print('-------------------------------------------')

class AnotherIterable:
    def __init__(self):
        self.cars = ['Fiesta', 'Focus']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]


for car in AnotherIterable():
    print(car)

# print(car)

print('--------------------------------------------')

my_numbers = [x for x in [1, 2, 3, 4, 5]]
my_numbers_gen = (x for x in [1, 2, 3, 4, 5])

print(type(my_numbers_gen))
print(next(my_numbers_gen))

for x in my_numbers_gen:
    print(x)
