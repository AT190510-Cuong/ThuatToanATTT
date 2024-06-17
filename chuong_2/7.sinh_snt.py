import random
t=30
def binh_phuong(a,k,n):
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

def is_prime(n, t):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    # Phân tích n - 1 thành dạng 2^s * r
    s = 0
    r = n - 1
    while r % 2 == 0:
        s += 1
        r //= 2
    # Thực hiện kiểm tra Miller-Rabin với t lần lặp
    for i in range(t):
        a=random.randint(2,n-1)
        y=binh_phuong(a,r,n)
        if(y!=1 and y!=(n-1)):
            j=1
            while(j<=(s-1) and y!=(n-1)):
                y=(y**2)%n
                if y==1:
                    return False
                j+=1
            if y!=(n-1):
                return False
    return True  

k=int(input('nhập k:'))
def generate_prime(k,t):
    if k < 2:
        return ("nhập số lớn hơn 1")
    while True:
        # Sinh ngẫu nhiên số có độ dài k bit
        n = random.getrandbits(k)
        # Kiểm tra số vừa sinh có phải là số nguyên tố hay không
        if is_prime(n, t):
            return n
    
print(generate_prime(k,t))
