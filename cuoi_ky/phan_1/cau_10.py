"""
Câu 10. Viết chương trình đếm số ước và
 số ước nguyên tố của một số N nhập vào từ bàn phím. ( đã tối ưu)
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


def divisor(n):
    d = [1, n]
    for i in range(2, int(math.sqrt(n) + 1)):
        if n / i == i:
            d.append(i)
            break
        if n % i == 0:
            d.append(i)
            d.append(n // i)
    return d


if __name__ == '__main__':
    n = int(input('Nhập số n = '))
    d = divisor(n)
    count_prime = 0
    for i in range(0, len(d)):
        if d[i] % 2 != 0 or d[i] == 2:
            if check_snt(d[i]):
                count_prime += 1
    print(d)
    print(f'Số ước = {len(d)}')
    print(f'Số ước nguyên tố = {count_prime}')
