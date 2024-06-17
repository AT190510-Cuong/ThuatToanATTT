"""
Câu 13. Viết chương trình tìm hai số nguyên tố nhỏ hơn hoặc bằng N
với N nhập vào từ bàn phím, sao cho tổng và hiệu của chúng đều
là số nguyên tố.
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


if __name__ == '__main__':
    n = int(input())
    r = []
    for i in range(2, n + 1):
        for j in range(i + 1, n + 1):
            if check_snt(i) and \
                    check_snt(j) \
                    and check_snt(i + j) \
                    and check_snt(j - i):
                r.append((i, j))
    if len(r) > 0:
        print(r)
    else:
        print(f'Danh sách rỗng ')
