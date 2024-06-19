'''
Câu 26. Một số được gọi là số mạnh mẽ khi nó đồng thời vừa chia hết
cho số nguyên tố và chia hết cho bình phương của số nguyên tố đó.
 Tìm số mạnh mẽ nhỏ hơn số N cho trước (N < 10000)
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


def number_strong(number_n):
    for x in range(number_n + 1):
        for i in range(2, int(x / 2) + 1):
            if check_snt(i) and x % i == 0 \
                    and x % (i * i) == 0:
                print(x, end=" ")
                break


if __name__ == '__main__':
    # number_n = int(input('Nhập n = '))
    while True:
        number_n = int(input('Nhập n = '))
        if 0 < number_n < 10000:
            break
        else:
            print('Nhập số nguyên dương nhỏ hơn 10000!')
    number_strong(number_n)
