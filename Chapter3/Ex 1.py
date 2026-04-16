km = float(input("Nhập số km đã đi: "))

if km <= 0:
    print("Số km không hợp lệ!")
elif km <= 1:
    tien = km * 15000
    print("Số tiền khách phải trả là:", tien, "VND")
elif km <= 20:
    tien = 15000 + (km - 1) * 12000
    print("Số tiền khách phải trả là:", tien, "VND")
else:
    tien = 15000 + 19 * 12000 + (km - 20) * 10000
    print("Số tiền khách phải trả là:", tien, "VND")