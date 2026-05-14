class BankAccount:
    # Hàm khởi tạo
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder   
        self.__balance = balance               

    # Hàm nạp tiền
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Nạp tiền thành công!")
        else:
            print("Số tiền nạp phải lớn hơn 0!")

    # Hàm rút tiền
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Rút tiền thành công!")
        else:
            print("Rút tiền thất bại!")

    # Getter lấy số dư
    def get_balance(self):
        return self.__balance


account1 = BankAccount("Nguyen Van A")

account1.deposit(500)

account1.withdraw(200)

account1.withdraw(1000)

print("Chủ tài khoản:", account1.account_holder)
print("Số dư hiện tại:", account1.get_balance())