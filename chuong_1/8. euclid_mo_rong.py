import math

a=int(input('nhap a :'))
b=int(input('nhap b :'))
def ucln(a,b):
    if b==0:
        d=a;x=1;y=0
    else:
        A=a
        B=b
        x2=1;x1=0
        y2=0;y1=1
        while(B>0):
            q=A//B
            r=A-q*B
            x=x2-q*x1
            y=y2-q*y1
            A=B;B=r
            x2=x1;x1=x
            y2=y1;y1=y
        d=A
        x=x2 
        y=y2 
        # if d==1:
        #     while(x<0 or y<0):
        #         if x<0:
        #             x+=b
        #         if y<0 :
        #             y+=a
        #     print('a^-1 mod b:',x)
        #     print('b^-1 mod a:',y)  
    return d, x, y
print('gcd=',ucln(a,b))    



