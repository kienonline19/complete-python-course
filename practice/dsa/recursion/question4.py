"""
n = 10
10/2 = 5r0
5/2 = 2r1
2/2 = 1r0
1/2 = 0r1
1 * 10 + 0 = 10
10 * 10 + 1 = 101
101 * 10 + 0 = 1010
d2b(1) = 1
d2b(n) = d2b(n // 2) * 10 + n % 2
"""
def decimal_to_binary(n):
    assert n >= 0 and int(n) == n, 'The number must be a positive integer only!'

    if n == 0:
        return 0

    return n % 2 + 10 * decimal_to_binary(int(n / 2))


print(decimal_to_binary(13))
print(decimal_to_binary(-13))
