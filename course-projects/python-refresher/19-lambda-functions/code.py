# def add(x, y):
#     return x + y

# add = lambda x,y: x + y
# print(add(5, 7))

# print((lambda x,y: x+y)(5, 7))

# def double(x):
#     return x * 2


sequence = [1, 3, 5, 9]
# doubled = [double(num) for num in sequence]

# print(doubled)

# doubled = list(map(double, sequence))
# print(doubled)

# print('-' * 20)

doubled = [(lambda x: x*2)(num) for num in sequence]
print(doubled)

doubled = list(map(lambda x: x*2, sequence))
print(doubled)
