# Hàm cộng
def cong(a, b):
    return a + b


# Hàm trừ
def tru(a, b):
    return a - b


# Hàm nhân
def nhan(a, b):
    return a * b


# Hàm chia
def chia(a, b):
    if b == 0:
        print("Lỗi chia cho 0")
    else:
        return a / b


# Hàm hiển thị menu
def hien_thi_menu():
    print("CALCULATOR BOT")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("5. Thoát")


# Luồng thực thi chính
while True:
    hien_thi_menu()
    lua_chon = input("Nhập lựa chọn của bạn: ")

    if lua_chon == "5":
        print("Kết thúc chương trình.")
        break

    elif lua_chon in ["1", "2", "3", "4"]:
        a = float(input("Nhập số a: "))
        b = float(input("Nhập số b: "))

        if lua_chon == "1":
            ket_qua = cong(a, b)
            print("Kết quả:", ket_qua)

        elif lua_chon == "2":
            ket_qua = tru(a, b)
            print("Kết quả:", ket_qua)

        elif lua_chon == "3":
            ket_qua = nhan(a, b)
            print("Kết quả:", ket_qua)

        elif lua_chon == "4":
            ket_qua = chia(a, b)
            if ket_qua is not None:
                print("Kết quả:", ket_qua)

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại.")