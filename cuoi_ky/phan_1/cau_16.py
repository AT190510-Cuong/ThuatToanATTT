"""
Câu 16. Viết chương trình tìm các số nguyên tố từ một
mảng sinh ngẫu nhiên có kích thước N,với N nhập vào
 từ bàn phím
"""

import math
import random

def check_snt(n):
    if n<2:
        return False
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n%i ==0:
                return False
        return True


def random_array(n):
    r = []
    for i in range(0, n):
        s = random.randint(2, 1000)
        r.append(s)
    return r


if __name__ == '__main__':
    # n = int(input('Nhập kích thước mảng = '))
    while True:
        n = int(input('Nhập kích thước mảng = '))
        if n > 0:
            break
        else:
            print("Nhập số nguyên dương lớn hơn 0!")
    a = random_array(n)
    print(a)
    r = []
    for i in range(0, len(a)):
        if a[i] % 2 != 0 or a[i] == 2:
            if check_snt(a[i]):
                r.append(a[i])
    if len(r) > 0:
        print(r)
    else:
        print('Danh sách rỗng ')
