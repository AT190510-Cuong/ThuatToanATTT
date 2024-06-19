import math

def tinh():
    # w=8
    # t=4
    # t=int(input('nhập t :'))
    p=int(input('nhap p :'))
    w=int(input('nhập w :'))
    m=round(math.log2(p),0)
    t=math.ceil(m/w)
    a=[]
    s=0
    print('nhập mảng A :')
    for i in range(t):
        x=int(input())
        a.append(x)
        s= s+a[i]*pow(2,(t-1-i)*w)
    return s
print('a =',tinh())        
    