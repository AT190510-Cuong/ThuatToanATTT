'''
Câu 24. Đặt S1, S2 là các mảng chứa giá trị bình phương của các số nguyên.
Hãy viết chương trình in ra số lượng tất cả các số nguyên tố nằm trong
 khoảng [a,b] sao cho số này cũng là tổngcủa hai số x và y với x thuộc
S1 và y thuộc S2. Trong đó, a,b là các số được nhập từ bàn phím
Ví dụ: với a=10, b =15, in ra giá trị là 1 vì trong khoảng [10,15]
chỉ có 2 số nguyên tố 11 và 13, nhưng chỉ có 13 = 2^2 + 3^2=4+9.

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


if __name__ == '__main__':
    # a = int(input('Nhập số a = '))
    # b = int(input(f'Nhập số b >='))
    while True:
        a = int(input('Nhập số a = '))
        b = int(input(f'Nhập số b >= {a} = '))
        if b >= a > 0:
            break
        else:
            print("Nhập số b lớn hơn hoặc bằng số a > 0!")
    l = []
    if b >= a:
        q = int(math.sqrt(b))
        for i in range(2, q + 1):
            for j in range(i, q + 1):
                if check_snt(i) and check_snt(j):
                    x = i * i + j * j
                    if check_snt(x) and x >= a and x <= b:
                        # print(i)
                        # print(j)
                        # print(x)
                        l.append(x)
    else:
        print('Thử Lại')

    print(len(l))
