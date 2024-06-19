"""
Câu 3. Cho một số nguyên dương N, gọi:
- k là số ước nguyên tố của N;
- q là tổng của các ước nguyên tố của N;
- p là tổng của các ước số của N;
- s là số ước của N;
Hãy viết chương trình tính giá trị của: N+p+s-q-k với N cho trước nhập từ bàn phím.
Ví dụ: N=24, có các ước là {1,2,3,4,6,8,12, 24} do đó:
p=1+2+3+4+6+8+12+24=60 và s=8
trong đó có 2 ước nguyên tố là {2,3} do đó:
q=2+3=5 và k=2
Và từ đó: N+p+s-q-k = 24+60+8-5-2=85;
"""
import math

def check_snt(n):
    if n<2:
        return False
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n%i ==0:
                return False
        return True


def divisor_prime(d): # tìm các ước nguyên tố
    p = []
    for i in d:
        if i %2 != 0 or i == 2:
            if check_snt(i):
                p.append(i)
    return p


def sum_divisor_prime(p):
    s = 0
    for e in p:
        s += e
    return s


def sum_divisor(d):
    s = 0
    for e in d:
        s += e
    return s


def divisor(n): # tìm các ước
    d = [1, n]
    for i in range(2, int(math.sqrt(n) + 1)):
        if n / i == i:
            d.append(i)
            break
        if n % i == 0:
            d.append(i)
            d.append(int(n / i))
    return d


if __name__ == '__main__':
    # n = int(input("nhap so n:"))
    while True:
        n = int(input("nhập sô n: "))
        if n >= 2:
            break 
        else:
            print("Nhập số nguyên dương lớn hơn 2!")
    d = divisor(n)
    num_prime = divisor_prime(d)
    k = len(num_prime)  # so uoc nt
    q = sum_divisor_prime(num_prime)  # tong ước nguyên tố
    p = sum_divisor(d)  # tổng ước
    s = len(d)
    print(n + p + s - q - k)
