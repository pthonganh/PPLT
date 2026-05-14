class Book:
    # Hàm khởi tạo
    def __init__(self, book_id, title, author, status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status

    # Hàm hiển thị thông tin sách
    def display_info(self):
        print("ID: ", self.book_id)
        print("Tên sách: ", self.title)
        print("Tác giả: ", self.author)
        print("Trạng thái: ", self.status)
        print("-------------------------")


class LibraryManager:
    # Hàm khởi tạo
    def __init__(self):
        self.book_list = []

    # Thêm sách mới
    def add_book(self, new_book):
        self.book_list.append(new_book)
        print("Thêm sách thành công!")

    # Hiển thị toàn bộ sách
    def display_all(self):
        if len(self.book_list) == 0:
            print("Thư viện chưa có sách!")
        else:
            print("--- DANH SÁCH SÁCH ---")
            for book in self.book_list:
                book.display_info()

    # Mượn sách
    def borrow_book(self, book_id):
        for book in self.book_list:
            if book.book_id == book_id:
                if book.status == "Available":
                    book.status = "Borrowed"
                    print("Mượn sách thành công!")
                else:
                    print("Sách đã được mượn!")
                return

        print("Không tìm thấy sách!")


# Hàm main
def main():
    # Tạo đối tượng quản lý thư viện
    manager = LibraryManager()

    while True:
        print("--- LIBRARY MANAGEMENT SYSTEM ---")
        print("1. Add a new book")
        print("2. Display all books")
        print("3. Borrow a book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # Thêm sách
        if choice == "1":
            book_id = input("Enter book ID: ")
            title = input("Enter title: ")
            author = input("Enter author: ")

            new_book = Book(book_id, title, author)
            manager.add_book(new_book)

        # Hiển thị sách
        elif choice == "2":
            manager.display_all()

        # Mượn sách
        elif choice == "3":
            book_id = input("Enter book ID to borrow: ")
            manager.borrow_book(book_id)

        # Thoát
        elif choice == "4":
            print("Program ended!")
            break

        else:
            print("Invalid choice!")


main()