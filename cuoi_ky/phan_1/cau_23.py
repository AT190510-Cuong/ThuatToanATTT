'''
Câu 23. Viết chương trình in ra màn hình YES trong trường hợp tổng
của các số nguyên tố trong khoảng [A, B] là cũng là một số nguyên tố
và NO nếu ngược lại. Với A,B là hai số được nhập vào từ bàn phím.
'''
import math

def check_snt(n):
    if n<2:
        return False
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n%i ==0:
                return False
        return True


def sum(number_a, number_b):
    value = 0
    for i in range(number_a, number_b + 1):
        if check_snt(i):
            value += i
    return value


if __name__ == '__main__':
    number_a = int(input('Nhập số a = '))
    number_b = int(input('Nhập số b = '))
    s = sum(number_a, number_b)
    if check_snt(s):
        print('YES')
    else:
        print('NO')
