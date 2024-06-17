import math

p=int(input('nhap p :'))
a=int(input('nhap a :'))
b=int(input('nhap b :'))

w=8
m=round(math.log2(p),0)
t=int(round((m/w),0))
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
P=bieu_dien_mang(p)

def chuyen_10_2(n):
    k = []
    while (n>0):
        a = n%2
        k.append(a) 
        n = n//2
    
    kq = ""
    for i in k:
        kq += str(i)
    while(len(kq)<16) :
        kq+='0'    
    return kq[::-1]
def chuyen_2_10(n):
    kq= int(n,2)
    return kq
A.reverse()
B.reverse()  
def nhan(A,B):
    C=[0]*(2*t)
    u=0
    kq=""
    for i in range(t):
        for j in range(t):
            UV=C[i+j]+A[i]*B[j]+u
            kq=chuyen_10_2(UV)
            U=kq[0:8]
            u=chuyen_2_10(U)
            V=kq[8::]
            v=chuyen_2_10(V)
            C[i+j]=v
        C[i+t]=u    
    C.reverse()
    return C
print('c =',nhan(A,B))    


