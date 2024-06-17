'''
Câu 44. Cho mảng A gồm các số nguyên thuộc 𝐹𝑝 nhập vào từ bàn phím,
hãy viết chương trình in ra mảng B có các phần tử là nghịch đảo của
các phần tử tương ứng trong A.
'''


def inversion(a,p):
    u = a
    v = p
    x1=1
    x2=0
    while(u !=1 ):
        q = v // u
        r=v-q*u
        x=x2-q*x1
        v=u
        u=r
        x2=x1
        x1=x
    return x1 % p


def gcd(a,b):
    while(b>0):
        r=a%b
        a=b
        b=r
    return a

p = int(input('P = '))
A = [int(x) for x in input().split()]
B = [0 for x in range(len(A))]

for i in range(0, len(A)):
    if gcd(A[i], p) == 1:  # gcd = 1 mới có nghịch đảo
        B[i] = inversion(A[i], p)
    else:
        B[i] = None
print(A)
print(B)
