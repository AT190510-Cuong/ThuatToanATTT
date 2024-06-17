"""
Câu 17. Viết chương trình tìm số nguyên dương x nhỏ nhất và nhỏ hơn N
 nhập từ bàn phím sao cho giá trị của biểu thức 𝐴𝑥2 + 𝐵𝑥 + 𝐶 là một số
 nguyên tố với A,B,C là các số nguyên nhập vào
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


def expression(number_n, number_a,number_b, number_c):
    for x in range(1, number_n + 1):
        s = number_a * x * x + number_b * x + number_c
        if check_snt(s):
            return s, x
    return None


if __name__ == '__main__':
    number_n = int(input('Nhập n = '))
    number_a = int(input('Nhập a = '))
    number_b = int(input('Nhập b = '))
    number_c = int(input('Nhập c = '))
    r = expression(number_n, number_a,number_b, number_c)
    if r != None:
        print(f'S = {r[0]}')
        print(f'X = {r[1]}')
    else:
        print('Không tồn tại số X')
