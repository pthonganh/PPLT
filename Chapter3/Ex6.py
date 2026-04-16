# Hàm thêm liên hệ mới
def add_contact(danh_ba):
    ten = input("Nhập tên liên hệ: ")
    sdt = input("Nhập số điện thoại: ")

    lien_he = ten + " - " + sdt
    danh_ba.append(lien_he)

    print("Đã thêm liên hệ thành công!")


# Hàm hiển thị liên hệ
def show_contacts(danh_ba):
    if len(danh_ba) == 0:
        print("Chưa có liên hệ nào.")
    else:
        print("Danh sách liên hệ:")
        for i in range(len(danh_ba)):
            print(str(i + 1) + ".", danh_ba[i])


# Hàm tìm kiếm liên hệ
def search_contact(danh_ba):
    ten_can_tim = input("Nhập tên cần tìm: ")
    tim_thay = False

    for lien_he in danh_ba:
        if ten_can_tim.lower() in lien_he.lower():
            print("Thông tin tìm thấy:", lien_he)
            tim_thay = True

    if tim_thay == False:
        print("Không tìm thấy.")


# Hàm main điều phối chương trình
def main():
    my_contacts = []

    while True:
        print("HỆ THỐNG QUẢN LÝ DANH BẠ")
        print("1. Thêm liên hệ mới")
        print("2. Hiển thị tất cả danh bạ")
        print("3. Tìm kiếm liên hệ")
        print("4. Thoát chương trình")
        print("===============================")

        lua_chon = input("Nhập lựa chọn của bạn (1-4): ")

        if lua_chon == "1":
            add_contact(my_contacts)

        elif lua_chon == "2":
            show_contacts(my_contacts)

        elif lua_chon == "3":
            search_contact(my_contacts)

        elif lua_chon == "4":
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")


# Kích hoạt chương trình
main()