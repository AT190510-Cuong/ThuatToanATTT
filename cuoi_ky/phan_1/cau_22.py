'''
Câu 22. Với một số nguyên dương N thoả mãn 0<N<10000, đặt:
F ( N ) = N nếu N là một số nguyên tố
F ( N ) = 0 nếu là hợp số
Cho L và R nhập vào từ bàn phím, với mọi cặp i , j trong
khoảng [ L , R ] hãy viết chương trình
in ra màn hình giá trị tổng của F ( i ) * F ( j ) với j > i.
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


def result(number_l, number_r):
    sum = 0
    for i in range(number_l, number_r):
        if check_snt(i):
            Fi = i
        else:
            Fi = 0
        for j in range(i + 1, number_r + 1):
            if check_snt(j):
                Fj = j
            else:
                Fj = 0
            sum += (Fi * Fj)
    return sum


if __name__ == '__main__':
    # number_l = int(input('Nhập số L = '))
    # number_r = int(input(f'Nhập số R > {number_l} = '))
    while True:
        number_l = int(input('Nhập số L = '))
        number_r = int(input(f'Nhập số R > {number_l} = '))
        if number_l > 0 and 10000 > number_r > number_l:
            break
        else:
            print("Nhập số nguyên dương lớn hơn 0 và số R lớn hơn số L!")
    if number_r > number_l:
        print(result(number_l, number_r))
    else:
        print('Thử Lại')
