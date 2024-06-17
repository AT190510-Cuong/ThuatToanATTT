import math
    
a=int(eval(input('nhap a :')))
p=int(input('nhap p :'))
w=int(input('nhap w :'))

# p=2147483647
# w=8

m=round(math.log2(p),0)
t=int(round((m/w),0))    

def bieu_dien_mang(a):
    l=[]
    d=0
    for i in range(t): 
        s=pow(2,(t-1-i)*w)
        x=(a-d)//s
        l.append(x)
        d+=x*s
    return l

print(('a được biểu diễn qua mảng :'),bieu_dien_mang(a))
