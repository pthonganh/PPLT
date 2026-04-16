
#Hàm tìm số lớn nhất
def find_max(lst):
    max_val = lst[0]  # giả sử phần tử đầu là lớn nhất
    
    for x in lst:
        if x > max_val:
            max_val = x
    
    return max_val

#Hàm tìm số nhỏ nhất
def find_min(lst):
    min_val = lst[0]  # giả sử phần tử đầu là nhỏ nhất
    
    for x in lst:
        if x < min_val:
            min_val = x
    
    return min_val

#Chạy thử
diem_so = [6.5, 8.0, 4.5, 9.5, 7.0]

print("Max:", find_max(diem_so))
print("Min:", find_min(diem_so))