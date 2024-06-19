"""
Câu 4. Viết chương trình đếm số số nguyên tố nằm trong khoảng [A,B]
với A, B nhập vào từ bàn phím
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
    # a = int(input("nhap a: "))
    # b = int(input("nhap b: "))
    while True:
        a = int(input("nhap a: "))
        b = int(input("nhap b: "))
        if 0 < a < b:
            break
        else:
            print("Nhập 0 < a < b!")
    count = 0
    for i in range(a, b + 1):
        if i % 2 != 0 or i == 2:
            if check_snt(i):
                count += 1
    print(count)
