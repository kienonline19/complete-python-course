kt_slp = lambda x: set(str(x)) == set('68')

for n in range(10000):
    if kt_slp(n):
        print(n, end=' ')
