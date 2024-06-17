T =input('TEXT T:')
P =input('TEXT P:')
#Hàm last_occurrence(P): Tạo một mảng L với độ dài 256, khởi tạo các phần tử của mảng bằng -1. Sau đó, lần lượt duyệt từng ký tự trong mẫu P và lưu vị trí xuất hiện cuối cùng của ký tự đó trong mẫu P vào mảng L. Cuối cùng, trả về mảng L này.
def last_occurrence(P):
    last = [-1] * 256
    for i in range(len(P)):
        last[ord(P[i])] = i
    return last
#Hàm boyer_moore(T,P): Sử dụng mảng L được tạo bởi hàm last_occurrence(P) để tìm kiếm mẫu P trong văn bản T. Đầu tiên, hàm tính độ dài của mẫu P và văn bản T. Sau đó, hàm duyệt văn bản T từ phải sang trái, tìm vị trí của từng ký tự trong mẫu P trong văn bản T. 
#Nếu tìm thấy một ký tự không khớp, hàm tính toán số bước dịch chuyển với giá trị m - min(j, 1 + L[ord(T[i])]), trong đó j là chỉ số của ký tự cuối cùng đã khớp và i là chỉ số của ký tự không khớp đó. Nếu mẫu P không xuất hiện trong văn bản T, hàm trả về chuỗi thông báo "P NOT IN T". 
#Nếu tìm thấy mẫu P, hàm trả về vị trí xuất hiện đầu tiên của mẫu P trong văn bản T.
def boyer_moore(T,P):
    L=last_occurrence(P)
    m=len(P)
    n=len(T)
    i=m-1
    while(i<n):
        j=m-1
        while(P[j]==T[i]):
            if j==0:
                return ('Vi tri xh T[{}]'.format(i))
            j-=1
            i-=1
        i=i+m-min(j,1+L[ord(T[i])])
    return ('P NOT IN T ')       
print(boyer_moore(T,P))

