'''
Câu 21. Một số gọi là siêu số nguyên tố nếu số lượng các số nguyên tố
từ 1 đến X (ngoại trừ X) là một số nguyên tố. Hãy viết chương trình
đếm số lượng các siêu số nguyên tố này trong khoảng [A,B] cho trước
nhập từ bàn phím
'''
import math

def check_snt(n):
    if n<2:
        return False
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n % i ==0:
                return False
        return True


def super_prime(number_a, number_b):
    result_list = []
    for x in range(number_a, number_b + 1):
        count = 0
        for i in range(1, x):
            if check_snt(i) and i % 2 != 0 or i == 2:
                count += 1
        if count % 2 != 0 or count == 2:
            if check_snt(count):
                result_list.append(x)
    return result_list


if __name__ == '__main__':
    # number_a = int(input('Nhập số a = '))
    # number_b = int(input(f'Nhập số b  > {number_a} =  '))
    while True:
        number_a = int(input('Nhập số a = '))
        number_b = int(input(f'Nhập số b  > {number_a} =  '))
        if number_b > number_a > 0:
            break
        else:
            print("Nhập số nguyên dương lớn hơn 0!")
    if number_b >= number_a >0 :
        result = super_prime(number_a, number_b)
        print(result)
        print(f'Có {len(result)} số siêu nguyên tố')
    else:
        print('Thử Lại')
