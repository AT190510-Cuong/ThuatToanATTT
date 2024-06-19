"""
Câu 7. Một số emirp là một số nguyên tố mà khi đảo ngược vị trí các chữ số của nó, ta cũng được
một số nguyên tố. Viết chương trình liệt kê các số emirp nhỏ hơn N với N nhập vào từ bàn phím.
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



def reverse(number):
    number_reverse = 0
    while number > 0:
        r = int(number % 10)
        number_reverse = number_reverse * 10 + r
        number = int(number / 10)
    return int(number_reverse)


if __name__ == '__main__':
    # number_n = int(input("Nhập n = "))
    while True:
        number_n = int(input("Nhập n = "))
        if number_n > 0:
            break
        else:
            print("Nhập số nguyên dương lớn hơn 0!")
    p = []
    for i in range(2, number_n + 1):
            if i % 2 != 0 or i == 2:
                if check_snt(i):
                    p.append(i)

    for i in range(2, number_n + 1):
        j = reverse(i)
        if i in p and j in p:
            print(i, end=" ")
