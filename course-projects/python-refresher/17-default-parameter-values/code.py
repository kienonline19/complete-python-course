def add(x, y=8):
    print(x + y)


def add(x=5, y=8):
    print(x + y)

# Default parameter values must go at the end
# def add(x=5, y):
#     print(x + y)


add()
add(5, 8)
add(5)
add(x=5)

# add(y=5) - TypeError
add(x=5, y=5)
# add(x=5, 5) - SyntaxError
