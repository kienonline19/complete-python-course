"""
GCD - ước chung lớn nhất là số nguyên dương lớn nhất 
mà những số chia cho nó không có một phần dư
Ví dụ:
GCD(8, 12) = 4
C1: phân tích thừa số nguyên tố của hai số
8 = 2 * 2 * 2
12 = 2 * 2 * 3
2 * 2 = 4
C2: giải thuật Euclidian
GCD(48, 18) = 6
b1: 48 / 18 = 2 dư 12
b2: 18 / 12 = 1 dư 6
b3: 12 / 6 = 2 dư 0
=> GCD = 6
GCD(a, 0) = a
GCD(a, b) = GCD(b, a mod b)
Đệ quy 3 bước:
b1: trường hợp đệ quy (flow): gcd(a, b) = gcd(b, a % b)
b2: trường hợp cơ sở (tiêu chí dừng): b = 0 -> a
b3: trường hợp không cố ý (ràng buộc): a, b là nguyên
chuyển đổi bất kỳ số âm nào thành dương (gcd của những số âm = gcd của những số dương thuộc cùng số)
"""
def gcd(a, b):
    assert int(a) == a and int(b) == b, 'The numbers must be integer only!'

    if a < 0:
        a = -a
    
    if b < 0:
        b = -b

    if b == 0:
        return a

    return gcd(b, a % b)


print(gcd(48, 18)) # 6
print(gcd(48, -18)) # 6
print(gcd(-48, 18)) # 6
print(gcd(0, 12)) # 12
print(gcd(1.2, 0)) # AssertionError
