try:
    so1 = int(input('Nhap so thu 1: '))
    so2 = int(input('Nhap so thu 2: '))

    tong = so1 + so2
    print('Tong hai so vua nhap la:', tong)
except EOFError as e:
    print(e)
