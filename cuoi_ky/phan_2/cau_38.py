'''
Câu 38. Tìm nghịch đảo của một số a trong trường 𝐹𝑝 với a và p
 được nhập từ bàn phím.
'''

def nghich_dao(a,p):
    u = a
    v = p
    x1=1
    x2=0
    while(u !=1 ):
        q = v // u
        r=v-q*u
        x=x2-q*x1
        v=u
        u=r
        x2=x1
        x1=x
    # return x1 % p
    return x1 


# p = int(input('Nhập số SNT P = '))
while True:
    p = int(input('Nhập số SNT P = '))
    if p > 1:
        break
    else:
        print("Nhập lại số P")
a = int(input(f'Nhập a = [1 {p - 1} ] = '))
print(nghich_dao(a, p))
