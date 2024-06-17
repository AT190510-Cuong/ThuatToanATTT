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
A.reverse()
B.reverse()

def tinh(x):
    s=0
    for i in range(t):
        s= s+x[i]*pow(2,(t-1-i)*w)
    return s
def cong(A,B): 
    A.reverse()
    B.reverse()
    C=[0]*t  
    e=0
    for i in range(t):
        s=A[i]+B[i]+e
        C[i]=s%(pow(2,w))
        if s< pow(2,w) :
            e=0
        else:
            e=1
    C.reverse()        
    return tinh(C)
def tru(A,B): 
    C=[0]*t    
    e=0
    for i in range(t):
        idx=0
        s=A[i]-B[i]-e
        if s<0:
            s=s+pow(2,w)
            idx=1
        C[i]=s%(pow(2,w))   
        if s>pow(2,w) or idx==1:
            e=1
        else:
            e=0
    C.reverse()        
    print('Tru chinh xac boi (e,C=A-B):({},{})'.format(e,C))
    if e==1 :
        return cong(C,P)
    else:
        return tinh(C)   
    
print('bieu dien p :',P)
print('Tru tren Fp :C = ',tru(A,B))

