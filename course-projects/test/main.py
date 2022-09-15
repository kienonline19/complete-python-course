from math import log10
n = 11223344556

length = int(log10(n)) + 1
m = n // 10 ** (length // 2)
print(m % 10) # 3
