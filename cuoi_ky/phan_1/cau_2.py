"""
Câu 2. Viết chương trình tìm các số nguyên tố có N chữ số với N nhập từ bàn phím và 2 ≤ N ≤
10
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
    number_n = int(input("nhập sô n: "))
    if number_n >= 2 and number_n <= 10:
        for i in range(int(10 ** (number_n - 1)), 10 ** number_n):
            if i % 2 != 0 or i == 2:
                if check_snt(i):
                    print(i)
    else:
        print("Vui lòng nhập 2 <= n <= 10")
