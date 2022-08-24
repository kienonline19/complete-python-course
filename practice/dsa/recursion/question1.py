"""
n = 1234
sum = 1 + 2 + 3 + 4 = 10

b1: f(n) = n % 10 + f(n // 10)
b2: n = 0 -> 0
b3: f(-1) ? f(1.5) ? -> infinite loops
"""
def sum_of_digits(n):
    assert n >= 0 and int(n) == n, 'The number has to be apositive integer only!'
    # print(f"{n} - remainder {int(n % 10)}")
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)


print(sum_of_digits(1234))
print(sum_of_digits(-10))

"""
n = 1234
f(1234) = 4 + f(123) = 10
f(123) = 3 + f(12) = 3
f(12) = 2 + f(1) = 3
f(1) = 1 + f(0) = 1
"""
