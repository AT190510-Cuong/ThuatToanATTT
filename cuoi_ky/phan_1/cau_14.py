"""
Câu 14. Viết chương trình tìm số nguyên tố có ba chữ số,
biết rằng nếu viết số đó theo thứ tự ngược lại thì ta được
một số là lập phương của một số tự nhiên.
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


def number_reverse(number):
    n_reverse = 0
    while number > 0:
        r = number % 10
        n_reverse = n_reverse * 10 + r
        number = int(number / 10)
    return int(n_reverse)


if __name__ == '__main__':
    min_number = 100
    max_number = 999
    a = int(100 ** (1 / 3))
    b = int(999 ** (1 / 3))
    for i in range(a, b + 1):
        reverse = number_reverse(i * i * i)
        if check_snt(reverse):
            print(reverse)
