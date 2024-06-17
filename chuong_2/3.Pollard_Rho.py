# Viết chương trình tìm một thừa số không tầm thường của một số n nhập từ bàn phím

n=int(input('nhap n:'))

def gcd(a,b):
    while(b>0):
        r=a%b
        a=b
        b=r
    return a

def thua_so_k_tam_thuong(n):
    a=2;b=2
    while(True):
        a=(a**2+1)%n
        b=(b**2+1)%n
        b=(b**2+1)%n
        d=gcd(a-b,n)
        if d>1 and d<n :
            d1=n/d
            print(n,'=',d,'*',d1)
            return
        elif d==n:
            print('Loss')
            return

thua_so_k_tam_thuong(n)