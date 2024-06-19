import math

n=int(input('nhap n:'))

def sang_PD(n):
    print('day snt <={} :'.format(n),end='')
    if n<2:
        print('nothing!')
    else:
        l=[True]*(n+1)
        denta=int(math.sqrt(n))
        for i in range(2,denta+2):
            if l[i]==True:   
                for j in range(i*2,denta+2,i):
                    l[j]=False
        d=1 
        check=0           
        while(check==0):
            for i in range(denta*d+2,denta*(d+1)+2):
                if (denta*(d+1)+2)>n:
                    check=1
                    m=n
                else:
                    m=denta*(d+1)+1
                p=int(math.sqrt(m))
                for i in range(2,p+1):
                    if l[i]==True:
                        for j in range(denta*d+2,m+1):
                            if(j%i==0):
                                l[j]=False
            d+=1
        for i in range(2,n+1):
            if l[i]==True:
                print(i,end=' ')  
                
sang_PD(n)                
