"""
Câu 5. Viết chương trình tính tổng của các số nguyên tố nằm trong khoảng [A, B] với A, B nhập
vào từ bàn phím.
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


if __name__ == '__main__':
    a = int(input("nhap a: "))
    b = int(input("nhap b: "))
    s = 0
    for i in range(a, b + 1):
        if i % 2 != 0 or i == 2:
            if check_snt(i):
                s += i
    print(s)
