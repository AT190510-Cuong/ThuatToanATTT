import math

p=int(input('nhap p :'))
w=int(input('nhap w :'))
# a=int(input('nhap a :'))
# b=int(input('nhap b :'))

m=round(math.log2(p),0)
t=math.ceil(m/w)





A = [0]*t 
B = [0]*t
C = [0]*t

print("Nhap vao mang A ")
for i in range(t):
    A[i] = int(input(f"Nhập vào phần tử A[{i}] : "))

print("Nhap vao mang B : ")
for i in range(t):
    B[i] = int(input(f"Nhập vào phần tử B[{i}] : "))






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

# A=bieu_dien_mang(a)
# B=bieu_dien_mang(b)
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
    return e,C

print('(e,C) = ',cong(A,B))             




