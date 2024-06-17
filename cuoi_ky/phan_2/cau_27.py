'''
Câu 27. Viết chương trình in ra các cặp số (a,b) thoả mãn điều kiện 0<a,b<1000,
sao cho ước chung lớn nhất của 2 số đó là một số nguyên tố.
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


def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


def find_pairs():
    """Tìm và in ra các cặp số (a, b) thoả mãn điều kiện đã cho."""
    pairs = []
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            if gcd(a, b) > 1:  # Tính ước chung lớn nhất
                if check_snt(gcd(a, b)):  # Kiểm tra ước chung lớn nhất có phải là số nguyên tố
                    pairs.append((a, b))
    return pairs

if __name__ == '__main__':
    pairs = find_pairs()
    if len(pairs) > 0:
        for pair in pairs:
            print(pair)
    else:
        print('a b không hợp lệ !')
