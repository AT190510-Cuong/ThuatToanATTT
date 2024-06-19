"""
Câu 15. Viết chương trình Hai số nguyên tố sinh đôi là hai số nguyên
tố hơn kém nhau 2 đơn vị.Tìm hai số nguyên tố sinh đôi nhỏ hơn hoặc
bằng N, với N được nhập vào từ bàn phím.
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


def twin_number(number_n):  # hiển thị kếtquar
    r = []
    for i in range(2, number_n - 1):  # duyệt 2 đến n
        if check_snt(i) and check_snt(i + 2):
            r.append((i, i + 2))
    return r


if __name__ == '__main__':
    # n = int(input('Nhập n = '))
    while True:
        n = int(input('Nhập n = '))
        if n > 2:
            break
        else:
            print("Nhập số nguyên dương lớn hơn 2!")
    r = twin_number(n)
    if len(r) > 0:
        print(r)
    else:
        print('Không tồn tại ')
