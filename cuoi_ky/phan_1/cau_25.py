'''
Câu 25. Cho 2 số M và N thoả mãn điều kiện: 1<=N<=10000; 2<M<=100;
Hãy viết chương trình xác định xem số N có thể được phân tích thành
tổng của M số nguyên tố hay không? Nếu có thì in
ra các số đó.
'''
import math
import itertools

# Hàm kiểm tra số nguyên tố
def check_snt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Hàm tạo danh sách các số nguyên tố nhỏ hơn max_n
def sieve_of_eratosthenes(max_n):
    primes = []
    for num in range(2, max_n + 1):
        if check_snt(num):
            primes.append(num)
    return primes

# Hàm chính để tìm tổng của M số nguyên tố bằng N
def find_prime_sum(N):
    primes = sieve_of_eratosthenes(10001)
    
    for M in range(3, 101):
        if N < 2 * M:
            continue  # Tổng của M số nguyên tố khác nhau nhỏ nhất luôn lớn hơn hoặc bằng 2M

        for combination in itertools.combinations(primes, M):
            if sum(combination) == N:
                return (M, combination)
    return None

# Hàm chính để in kết quả
if __name__ == '__main__':
    # N = int(input("Nhập số N: "))
    while True: 
        N = int(input("Nhập số N: "))
        if 1 <= N <= 10000:
            break
        else:
            print("Nhập số nguyên dương N trong khoảng từ 1 đến 10000.")
    result = find_prime_sum(N)
    if result:
        M, combination = result
        print(f"Tìm thấy {M} số nguyên tố có tổng bằng {N}: {combination}")
    else:
        print(f"Không tìm thấy tổ hợp {M} số nguyên tố thỏa mãn.")




