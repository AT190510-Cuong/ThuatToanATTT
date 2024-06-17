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

def miller_rabin(n):
    if n<2:
        return('nhập số lớn hơn 2 !')
    if n==2:
        return('nguyên tố !')
    elif n%2==0 :
        return('Hợp số')  
    
    r=n-1
    s=0
    while(r%2==0):
        s+=1
        r=r//2
    # t>=1     
    t=20
    for i in range(t):
        a=random.randint(2,n-2)
        # a=2
        y=binh_phuong(n,a,r)
        if(y!=1 and y!=(n-1)):
            j=1
            while(j<=(s-1) and y!=(n-1)):
                y=(y**2)%n
                if y==1:
                    return ('Hợp số')
                j+=1
            if y!=(n-1):
                return('Hợp số')
    return ('nguyên tố !')   
print(miller_rabin(n))   





