'''
Câu 30. Viết chương trình tính tổng của các số Carmichael
(là các số giả nguyên tố n thoả mãn điều kiện là hợp số
và thoả mãn 𝑏𝑛−1 ≡ 1 (𝑚𝑜𝑑 𝑛) với mọi số nguyên dương b
 nguyên tố cùng nhau với n) nhỏ hơn một số N cho trước nhập
 vào từ bàn phím (với điều kiện 0 ≤ 𝑁 ≤ 10000.
'''
import math


def is_prime(number):
    if number < 2:
        return False
    for x in range(2, int(math.sqrt(number) + 1)):
        if number % x == 0:
            return False
    return True


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


def gcd(x, number_n):
    if number_n == 0:
        return x
    return gcd(number_n, x % number_n)


def check(i):
    for x in range(1, i):
        if gcd(x, i) == 1:
            if (binh_phuong(x, i - 1, i) != 1):
                return False
    return True


def sum_number_carmichael(number_n):
    sum = 0
    for i in range(31, number_n + 1, 2):
        if is_prime(i) == False:
            if check(i):
                sum += i
    print(sum)


# number_n = int(input("nhap so N:"))
while True:
    number_n = int(input("nhập số N ="))
    if number_n >= 0 and number_n <= 10000:
        break
    else:
        print("Nhập lại số N")
sum_number_carmichael(number_n)
