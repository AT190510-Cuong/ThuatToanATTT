import random
n=int(input('nhap n:'))

def binh_phuong(n,a,k):
    b=1
    if k==0:
        return b
    l = []
    while (k>0):
        x = k%2
        l.append(x) 
        k = k//2
    kq = ""
    for i in l:
        kq += str(i)  
    A=a
    if kq[0]=='1':
        b=a
    for i in range(1,len(kq)):
        A=(A**2)%n
        if kq[i]=='1':
            b=(A*b)%n
    return b     

def fermat(n):
    if n==2:
        return ("số nguyên tố")
    if n<2:
        return ('nhập số lớn hơn 2')
    
    t=50
    for i in range(t):
        a=random.randint(2,n-2)
        # print('a =',a)
        # a=2
        r=binh_phuong(n,a,n-1)
        if r!=1:
            return ('Hợp số')        
    return ('Chắc là số nguyên tố')
print(fermat(n))        