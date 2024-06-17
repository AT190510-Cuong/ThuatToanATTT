T =input('TEXT T:')
P =input('TEXT P:')
def vet_can(T,P):
    for i in range(len(T)-len(P)+1):
        j=0
        while(P[j]==T[i]):
            j+=1
            i+=1
            if j==len(P) :
                return ('T[{}]'.format(i-j))
    return (' P Not IN T ')
print('Vi tri xh :',vet_can(T,P))
