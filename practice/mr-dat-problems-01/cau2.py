import random


# Cau 2a
def tao_ds_ngau_nhien():
    while True:
        try:
            n = int(input("Nhap vao so nguyen duong n: "))

            if n < 10 or n > 1000:
                print("Chi nhan gia tri tu 10 den 1000. Yeu cau nhap lai")
            else:
                break
        except:
            print("Phai nhap vao so nguyen duong. Yeu cau nhap lai")

    return random.sample(range(1, 2001), int(n))


lst = tao_ds_ngau_nhien()
print(lst)

# Cau 2b


def kiem_tra_smm(n):
    past = set()
    tmp = n
    flag = True

    while tmp != 1:
        tmp = sum(int(i) ** 2 for i in str(tmp))

        if tmp in past:
            flag = False
            break

        past.add(tmp)

    return flag


ds_smm = [x for x in lst if kiem_tra_smm(x)]

if len(ds_smm) == 0:
    print("Trong danh sach khong chua so may man")
else:
    print("Cac so may man trong danh sach la", end=' ')
    print(*ds_smm)

# Cau 2c


def is_strobogrammatic(num):
    res = ''

    for i in range(len(num)):
        n = ord(num[i]) - 48

        if n in {2, 3, 4, 5, 7}:
            return False
        elif n in {1, 8, 0}:
            res = str(n) + res
        elif n == 9:
            res = '6' + res
        else:
            res = '9' + res

    return res == num


def is_prime(N):
    if N < 2:
        return False

    for x in range(2, int(N ** 0.5) + 1):
        if not N % x:
            return False

    return True


ds = [x for x in lst if is_prime(x) and is_strobogrammatic(str(x))]

if len(ds) == 0:
    print("Trong danh sach khong chua so vua nguyen to vua strobogrammatic")
else:
    print("Cac so so vua nguyen to vua strobogrammatic trong danh sach la", end=' ')
    print(*ds)
