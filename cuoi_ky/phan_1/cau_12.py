"""
Câu 12. Viết chương trình tìm bốn số nguyên tố liên tiếp,
 sao cho tổng của chúng là số nguyên tố
nhỏ hơn hoặc bằng N (với N được nhập vào từ bàn phím).( đã tối ưu)
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


def sum_sub(sub):
    s = 0
    for e in sub:
        s += e
    return s


def list_number_prime(n):
    p = []
    for i in range(n):
        if check_snt(i):
            p.append(i)
    return p


if __name__ == '__main__':
    # number_n = int(input("Nhập n = "))
    while True:
        number_n = int(input('Nhập n = '))
        if number_n > 2:
            break
        else:
            print("Nhập số nguyên dương lớn hơn 2!")
    if number_n < 17:
        print("NO")
    else:
        i = 0
        p = list_number_prime(number_n)
        while i + 4 <= len(p):  
            sub = p[i:i + 4]
            s = sum_sub(sub)
            if  (s < number_n) and (s % 2 != 0 or s == 2):
                if check_snt(s):
                    print(sub)
                # pass
            i += 1
