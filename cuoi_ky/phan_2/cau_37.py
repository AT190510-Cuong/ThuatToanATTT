'''
Câu 37. Lập trình tìm kiếm xâu S1 trong xâu S2 theo thuật toán Knutt-Morris-Patt.
Trong trường hợp nào thì thuật toán Boyer-Moore được xem là cải tiến hơn
 thuật toán tìm kiếm vét cạn?
'''


T =input('TEXT T:')
P =input('TEXT P:')

def failure_function(P):
    F=[-1,0]
    for j in range(2,len(P)):
        d=0
        t=1
        i=j-1
        x=j
        while(t<j):
            if P[0:t]==P[i:x]:
                d+=1
            t+=1
            i-=1
        F.append(d)
    return F

def kmp(P,T):
    F=failure_function(P)
    i,j,t=0,0,0
    while(i<len(T)):
        if T[i]==P[j]:
            i+=1
            j+=1
            if j == len(P):
                return ('Vi tri xh T[{}]'.format(i-j))
        else:
            if t==0:
                i=j-F[j] 
            elif t!=0 :
                i=i+j-F[j]
            while(1):
                if F[j]!=-1:
                    j=F[j]  
                else: 
                    j=0
                break
            t=1
    return('P NOT IN T')

print(kmp(P,T))    
# print(failure_function(P))    
