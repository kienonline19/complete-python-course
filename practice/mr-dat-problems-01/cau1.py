def fibo(n):
    if n in {0, 1}:
        return n
    return fibo(n - 1) + fibo(n - 2)


n = int(input("Nhap vao so nguyen duong n: "))

while n <= 1:
    n = int(input("Nhap vao so nguyen duong n: "))

for x in range(n):
    print(fibo(x), end=' ')
