# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

n = int(input("Nhập n: "))
print(is_prime(n))

# In các số nguyên tố từ 1 đến 100
print("Các số nguyên tố từ 1 đến 100 là:")
for i in range(1, 101):
    if is_prime(i):
        print(i, end=" ")