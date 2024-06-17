import math

p=int(input('nhap p :'))
w=int(input('nhap w :'))
a=int(input('nhap a :'))
b=int(input('nhap b :'))

# p=2147483647
# w=8
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
    # return e,tinh(C)
    return e,C

print('(e,C) = ',tru(A,B))    

