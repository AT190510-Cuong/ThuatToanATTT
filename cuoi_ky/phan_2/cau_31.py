'''
Câu 31. Áp dụng theo các thuật toán đã được học trong phần lí thuyết
em hãy cài đặt chương trình:
- Tìm số nguyên tố k gần nhất với phần số của mã số sinh viên của mình
(trong trường hợp khoảng cách bằng nhau thì lấy số nhỏ hơn).
- Từ số k tìm được tính ak mod n với a = SBD, n = 123456
'''
import math
import random

def square_integer(a, r, n):
    k = []
    while r > 0:
        k.append(r % 2)
        r //= 2
    temp = a
    if k[0] == 1:
        b = a
    else:
        b = 1
    for i in range(1, len(k)):
        temp = (temp * temp) % n
        if k[i] == 1:
            b = (b * temp) % n
    return b


def SoNguyenTo(n):  # dùng miller để xét nguyên tố
    t = 50
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    s = 0
    x = n - 1
    while x % 2 == 0:
        s += 1
        x //= 2
    r = x
    for i in range(1, t + 1):
        a = random.randint(2, n - 2)
        y = square_integer(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = y ** 2 % n
                if y == 1:
                    return False
                j += 1
            if y != n - 1:
                return False
    return True

# hàm chứng minh snt
# def SoNguyenTo(n):
#     # if n == 2:
#     #     return False
#     for i in range(2, int(math.sqrt(n) + 1)):
#         if n % i == 0:
#             return False
#     return True


def SoNhoHonMSV(msv):
    while True:
        if SoNguyenTo(msv):
            return msv
        msv -= 1


def SoLonHonMSV(msv):
    while True:
        if SoNguyenTo(msv):
            return msv
        msv += 1


def TimSoGanMSV(msv):  # tím số nguyên tố nhỏ ,lớn gần nhất vs msv
    soNho = SoNhoHonMSV(msv)
    soLon = SoLonHonMSV(msv + 1)
    if msv - soNho > soLon - msv:  # khoảng cách sosos nhỏ - msv lớn hơn số lớn -msv ,lấy số lớn
        return soLon
    else:
        return soNho  # nguwjojc lại


def binh_phuong(a,k,n):
    b=1
    if k==0:
        return b
    # chuyển k sang hệ nhị phân và lưu vào mảng l sau đó đảo ngược mảng l
    l = []
    while (k>0):
        x = k%2
        l.append(x) 
        k = k//2
    kq = ""
    for i in l:
        kq += str(i) 

    A=a
    if kq[0]=='1':
        b=a
    for i in range(1,len(kq)):
        A=(A**2)%n
        if kq[i]=='1':
            b=(A*b)%n
    return b    


a = int(input('SBD = '))
msv = int(input('MSV = '))
k = TimSoGanMSV(msv)
print(k)
n = 123456
print(binh_phuong(a, k, n))
