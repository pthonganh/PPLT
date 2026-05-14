class Pet:
    # Hàm khởi tạo
    def __init__(self, pet_id, name, species, price):
        self.__pet_id = pet_id      
        self.name = name
        self.species = species
        self.price = price

    # Getter lấy mã thú cưng
    def get_pet_id(self):
        return self.__pet_id

    # Hiển thị
    def display_info(self):
        print("ID: ", self.__pet_id)
        print("Tên thú cưng: ", self.name)
        print("Loài: ", self.species)
        print("Giá: ", self.price)
        print("-------------------------")


class StoreService:
    # Hàm khởi tạo
    def __init__(self):
        self.inventory = []
        self.revenue = 0.0

    # Thêm thú cưng mới
    def add_pet(self, pet):
        self.inventory.append(pet)
        print("Thêm thú cưng thành công!")

    # Xem danh sách thú cưng
    def view_inventory(self):
        if len(self.inventory) == 0:
            print("Cửa hàng hiện chưa có thú cưng nào!")
        else:
            print("--- DANH SÁCH THÚ CƯNG ---")
            for pet in self.inventory:
                pet.display_info()

    # Bán thú cưng
    def sell_pet(self, pet_id):
        for pet in self.inventory:
            if pet.get_pet_id() == pet_id:
                self.inventory.remove(pet)
                self.revenue += pet.price
                print("Bán thú cưng thành công!")
                return

        print("Không tìm thấy thú cưng!")

    # Xem tổng doanh thu
    def view_total_revenue(self):
        print("Tổng doanh thu:", self.revenue)


class ConsoleView:
    # Hàm khởi tạo
    def __init__(self):
        self.store_service = StoreService()

    # Menu chương trình
    def run(self):
        while True:
            print("--- PET STORE MANAGEMENT APP ---")
            print("1. Add a new pet")
            print("2. View inventory")
            print("3. Sell a pet")
            print("4. View total revenue")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                pet_id = input("Enter pet ID: ")
                name = input("Enter pet name: ")
                species = input("Enter species: ")
                price = float(input("Enter price: "))

                new_pet = Pet(pet_id, name, species, price)
                self.store_service.add_pet(new_pet)

            elif choice == "2":
                self.store_service.view_inventory()

            elif choice == "3":
                pet_id = input("Enter pet ID to sell: ")
                self.store_service.sell_pet(pet_id)

            elif choice == "4":
                self.store_service.view_total_revenue()

            elif choice == "5":
                print("Program ended!")
                break

            else:
                print("Invalid choice!")


app = ConsoleView()
app.run()