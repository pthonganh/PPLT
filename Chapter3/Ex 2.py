n = int(input("Nhập số nguyên dương n: "))

if n <= 0:
    print("n là số nguyên dương.")
else:
    tong_chan = 0
    tong_le = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            tong_chan += i
        else:
            tong_le += i

    print("Tổng số lẻ:", tong_le)
    print("Tổng số chẵn:", tong_chan)