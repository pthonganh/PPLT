from models.standard_room import StandardRoom
from models.vip_room import VIPRoom
from models.villa_room import VillaRoom
from models.customer import Customer


class MenuView:

    def __init__(
        self,
        room_service,
        customer_service,
        booking_service,
        report_service
    ):
        self.room_service = room_service
        self.customer_service = customer_service
        self.booking_service = booking_service
        self.report_service = report_service

    def run(self):

        while True:

            print("========== HOTEL RESORT MANAGEMENT ==========")
            print("1. Room Management")
            print("2. Customer Management")
            print("3. Booking Management")
            print("4. Reports")
            print("0. Exit")

            choice = input("Choose: ")

            if choice == "1":
                self.room_menu()

            elif choice == "2":
                self.customer_menu()

            elif choice == "3":
                self.booking_menu()

            elif choice == "4":
                self.report_menu()

            elif choice == "0":

                self.room_service.save_data()
                self.customer_service.save_data()
                self.booking_service.save_data()

                print("Data saved successfully!")
                print("Goodbye!")

                break

            else:
                print("Invalid choice!")

    # ==================================
    # ROOM MENU
    # ==================================

    def room_menu(self):

        while True:

            print("========== ROOM MANAGEMENT ==========")
            print("1. Add Room")
            print("2. View Rooms")
            print("3. Update Room")
            print("4. Delete Room")
            print("5. Search Room")
            print("6. Sort Price Asc")
            print("7. Sort Price Desc")
            print("0. Back")

            choice = input("Choose: ")

            if choice == "1":
                self.add_room()

            elif choice == "2":
                self.view_rooms()

            elif choice == "3":
                self.update_room()

            elif choice == "4":
                self.delete_room()

            elif choice == "5":
                self.search_room()

            elif choice == "6":
                self.sort_room_asc()

            elif choice == "7":
                self.sort_room_desc()

            elif choice == "0":
                break

            else:
                print("Invalid choice!")

    def add_room(self):

        try:

            room_id = input("Room ID: ")

            room_type = input(
                "Type (Standard/VIP/Villa): "
            )

            price = float(
                input("Price per day: ")
            )

            capacity = int(
                input("Capacity: ")
            )

            if room_type.lower() == "standard":

                room = StandardRoom(
                    room_id,
                    price,
                    capacity
                )

            elif room_type.lower() == "vip":

                room = VIPRoom(
                    room_id,
                    price,
                    capacity
                )

            elif room_type.lower() == "villa":

                room = VillaRoom(
                    room_id,
                    price,
                    capacity
                )

            else:

                print("Invalid room type!")
                return

            self.room_service.add_room(room)

            print("Room added successfully!")

        except Exception as e:

            print("Error:", e)

    def view_rooms(self):

        rooms = self.room_service.get_all_rooms()

        if len(rooms) == 0:

            print("No rooms found.")
            return

        print("========== ROOM LIST ==========")

        for room in rooms:

            print(
                f"{room.room_id} | "
                f"{room.get_room_type()} | "
                f"{room.price} | "
                f"{room.capacity} | "
                f"{room.status}"
            )

    def delete_room(self):

        room_id = input("Enter Room ID: ")

        if self.room_service.delete_room(room_id):

            print("Deleted successfully!")

        else:

            print("Room not found!")

    def update_room(self):

        room_id = input("Room ID: ")

        price = float(input("New Price: "))
        capacity = int(input("New Capacity: "))

        if self.room_service.update_room(
            room_id,
            price,
            capacity
        ):
            print("Updated successfully!")
        else:
            print("Room not found!")

    def search_room(self):

        keyword = input("Keyword: ")

        rooms = self.room_service.search_room(
            keyword
        )

        for room in rooms:

            print(
                f"{room.room_id} | "
                f"{room.get_room_type()} | "
                f"{room.price}"
            )

    def sort_room_asc(self):

        rooms = self.room_service.sort_by_price_ascending()

        for room in rooms:

            print(
                f"{room.room_id} | "
                f"{room.price}"
            )

    def sort_room_desc(self):

        rooms = self.room_service.sort_by_price_descending()

        for room in rooms:

            print(
                f"{room.room_id} | "
                f"{room.price}"
            )
        # ==================================
    # CUSTOMER MENU
    # ==================================

    def customer_menu(self):

        while True:

            print("========== CUSTOMER MANAGEMENT ==========")
            print("1. Add Customer")
            print("2. View Customers")
            print("3. Update Customer")
            print("4. Delete Customer")
            print("5. Search Customer")
            print("0. Back")

            choice = input("Choose: ")

            if choice == "1":
                self.add_customer()

            elif choice == "2":
                self.view_customers()

            elif choice == "3":
                self.update_customer()

            elif choice == "4":
                self.delete_customer()

            elif choice == "5":
                self.search_customer()

            elif choice == "0":
                break

            else:
                print("Invalid choice!")

    def add_customer(self):

        try:

            customer_id = input("Customer ID: ")
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")

            customer = Customer(
                customer_id,
                name,
                phone,
                email
            )

            self.customer_service.add_customer(
                customer
            )

            print("Customer added successfully!")

        except Exception as e:

            print("Error:", e)

    def view_customers(self):

        customers = self.customer_service.get_all_customers()

        if len(customers) == 0:

            print("No customers found.")
            return

        print("========== CUSTOMER LIST ==========")

        for customer in customers:

            print(
                f"{customer.customer_id} | "
                f"{customer.name} | "
                f"{customer.phone} | "
                f"{customer.email}"
            )

    def delete_customer(self):

        customer_id = input(
            "Enter Customer ID: "
        )

        if self.customer_service.delete_customer(
            customer_id
        ):

            print(
                "Deleted successfully!"
            )

        else:

            print(
                "Customer not found!"
            )

    def update_customer(self):

        customer_id = input(
            "Customer ID: "
        )

        name = input("New Name: ")
        phone = input("New Phone: ")
        email = input("New Email: ")

        if self.customer_service.update_customer(
            customer_id,
            name,
            phone,
            email
        ):
            print("Updated successfully!")
        else:
            print("Customer not found!")

    def search_customer(self):

        keyword = input(
            "Customer Name: "
        )

        customers = (
            self.customer_service
            .search_customer_by_name(
                keyword
            )
        )

        for customer in customers:

            print(
                f"{customer.customer_id} | "
                f"{customer.name} | "
                f"{customer.phone}"
            )

    
    # ==================================
    # BOOKING MENU
    # ==================================

    def booking_menu(self):

        while True:

            print("========== BOOKING MANAGEMENT ==========")
            print("1. Create Booking")
            print("2. View Bookings")
            print("3. Cancel Booking")
            print("0. Back")

            choice = input("Choose: ")

            if choice == "1":
                self.create_booking()

            elif choice == "2":
                self.view_bookings()

            elif choice == "3":
                self.cancel_booking()

            elif choice == "0":
                break

            else:
                print("Invalid choice!")

    def create_booking(self):

        try:

            booking_id = input("Booking ID: ")

            customer_id = input(
                "Customer ID: "
            )

            room_id = input(
                "Room ID: "
            )

            check_in = input(
                "Check In (YYYY-MM-DD): "
            )

            check_out = input(
                "Check Out (YYYY-MM-DD): "
            )

            booking = self.booking_service.create_booking(
                booking_id,
                customer_id,
                room_id,
                check_in,
                check_out
            )

            print(
                "Booking created successfully!"
            )

            print(
                f"Total Price: {booking.total_price}"
            )

        except Exception as e:

            print("Error:", e)

    def view_bookings(self):

        bookings = self.booking_service.get_all_bookings()

        if len(bookings) == 0:

            print("No bookings found.")
            return

        print("========== BOOKING LIST ==========")

        for booking in bookings:

            print(
                f"{booking.booking_id} | "
                f"{booking.customer_id} | "
                f"{booking.room_id} | "
                f"{booking.check_in} | "
                f"{booking.check_out} | "
                f"{booking.total_price}"
            )

    def cancel_booking(self):

        booking_id = input(
            "Booking ID: "
        )

        if self.booking_service.cancel_booking(
            booking_id
        ):

            print(
                "Booking cancelled!"
            )

        else:

            print(
                "Booking not found!"
            )

    # ==================================
    # REPORT MENU
    # ==================================

    def report_menu(self):

        while True:

            print("========== REPORTS ==========")
            print("1. Total Revenue")
            print("2. Available Rooms")
            print("3. Booked Rooms")
            print("4. Export Booking CSV")
            print("0. Back")

            choice = input("Choose: ")

            if choice == "1":
                self.show_revenue()

            elif choice == "2":
                self.show_available_rooms()

            elif choice == "3":
                self.show_booked_rooms()

            elif choice == "4":
                self.export_csv()

            elif choice == "0":
                break

            else:
                print("Invalid choice!")

    def show_revenue(self):

        revenue = (
            self.report_service
            .get_total_revenue()
        )

        print(
            f"Total Revenue: {revenue}"
        )

    def show_available_rooms(self):

        rooms = (
            self.report_service
            .get_available_rooms()
        )

        print(
            "===== AVAILABLE ROOMS ====="
        )

        for room in rooms:

            print(
                f"{room.room_id} | "
                f"{room.get_room_type()} | "
                f"{room.price}"
            )

    def show_booked_rooms(self):

        rooms = (
            self.report_service
            .get_booked_rooms()
        )

        print(
            "===== BOOKED ROOMS ====="
        )

        for room in rooms:

            print(
                f"{room.room_id} | "
                f"{room.get_room_type()} | "
                f"{room.price}"
            )

    def export_csv(self):

        self.report_service.export_bookings_csv()

        print(
            "booking_report.csv exported successfully!"
        )