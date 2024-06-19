"""
Câu 11. Viết chương trình tính tổng của các số nguyên tố nhỏ hơn hoặc bằng N với N được nhập
từ bàn phím.
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
    # n = int(input('Nhập n = '))
    while True:
        n = int(input('Nhập n = '))
        if n > 2:
            break
        else:
            print("Nhập số nguyên dương lớn hơn 2!")
    s = 0
    for i in range(2, n + 1):
        if i % 2 != 0 or i == 2:
            if check_snt(i):
                s += i
    print(s)
