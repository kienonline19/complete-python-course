"""
b1: x^n = x * x^(n - 1)
b2: n = 0 (1), n = 1 (x)
b3: f(-3.2), f(3.2, 2), f(2, 1.5), f(2, -1)
"""
def power(base, exp):
    assert exp >= 0 and int(exp) == exp, 'The exponent must be a positive integer only!'

    if exp == 0:
        return 1

    if exp == 1:
        return base

    return base * power(base, exp - 1)


print(power(4, 3)) # 64
print(power(-1, -4))
