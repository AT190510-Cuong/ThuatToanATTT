"""
Câu 18. Áp dụng thuật toán đã được học để viết chương trình tính tổng của hai số nguyên lớn,
hiển thị dưới mạng mảng và dạng số nguyên
"""
import math

p=int(input('nhap p :'))
# p = 2147483647
w=int(input('nhap w :'))
# w=8
a=int(input('nhap a :'))
b=int(input('nhap b :'))

m=round(math.log2(p),0)
t=math.ceil(m/w)






def tinh(x):
    s=0
    for i in range(t):
        s= s+x[i]*pow(2,(t-1-i)*w)
    return s
def bieu_dien_mang(a):
    l=[]
    d=0
    for i in range(t): 
        s=(pow(2,(t-1-i)*w))
        x=(a-d)//s
        l.append(x)
        d+=x*s
    return(l)

A=bieu_dien_mang(a)
B=bieu_dien_mang(b)
A.reverse()
B.reverse()

def cong(A,B): 
    C=[0]*t  
    e=0
    for i in range(t):
        s=A[i]+B[i]+e
        C[i]=s%(pow(2,w))
        if s < pow(2,w) :
            e=0
        else:
            e=1
    C.reverse()        
    # return e,tinh(C)
    return C

print('(e,C) = ',cong(A,B))             
print('(e,C) = ',tinh(cong(A,B)))







