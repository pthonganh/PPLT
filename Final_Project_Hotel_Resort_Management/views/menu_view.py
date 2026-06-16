from models.standard_room import StandardRoom
from models.vip_room import VIPRoom
from models.villa_room import VillaRoom
from models.customer import Customer
from prettytable import PrettyTable


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

    # ==================================
    # PRETTY TABLE HELPERS
    # ==================================

    def print_rooms_table(self, rooms):

        if len(rooms) == 0:
            print("No rooms found.")
            return

        table = PrettyTable()

        table.field_names = [
            "Room ID",
            "Type",
            "Price",
            "Capacity",
            "Status",
            "Services"
        ]

        table.align = "l"

        for room in rooms:
            table.add_row([
                room.room_id,
                room.get_room_type(),
                room.price,
                room.capacity,
                room.status,
                ", ".join(room.get_services())
            ])

        print(table)

    def print_customers_table(self, customers):

        if len(customers) == 0:
            print("No customers found.")
            return

        table = PrettyTable()

        table.field_names = [
            "Customer ID",
            "Name",
            "Phone",
            "Email"
        ]

        table.align = "l"

        for customer in customers:
            table.add_row([
                customer.customer_id,
                customer.name,
                customer.phone,
                customer.email
            ])

        print(table)

    def print_bookings_table(self, bookings):

        if len(bookings) == 0:
            print("No bookings found.")
            return

        table = PrettyTable()

        table.field_names = [
            "Booking ID",
            "Customer ID",
            "Room ID",
            "Check In",
            "Check Out",
            "Total Price"
        ]

        table.align = "l"

        for booking in bookings:
            table.add_row([
                booking.booking_id,
                booking.customer_id,
                booking.room_id,
                booking.check_in,
                booking.check_out,
                booking.total_price
            ])

        print(table)

    def print_revenue_table(self, revenue_data):

        if len(revenue_data) == 0:
            print("No revenue data found.")
            return

        table = PrettyTable()

        table.field_names = [
            "Room Type",
            "Revenue"
        ]

        table.align = "l"

        for room_type, revenue in revenue_data.items():
            table.add_row([
                room_type,
                revenue
            ])

        print(table)

    def print_room_statistics_table(self, stats):

        if len(stats) == 0:
            print("No room statistics found.")
            return

        table = PrettyTable()

        table.field_names = [
            "Room Type",
            "Total Rooms"
        ]

        table.align = "l"

        for room_type, total in stats.items():
            table.add_row([
                room_type,
                total
            ])

        print(table)

    # ==================================
    # MAIN MENU
    # ==================================

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
            print("8. Sort Capacity Asc")
            print("9. Sort Capacity Desc")
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

            elif choice == "8":
                self.sort_capacity_asc()

            elif choice == "9":
                self.sort_capacity_desc()

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

        print("========== ROOM LIST ==========")

        self.print_rooms_table(rooms)

    def delete_room(self):

        try:

            room_id = input("Enter Room ID: ")

            if self.room_service.delete_room(room_id):
                print("Deleted successfully!")
            else:
                print("Room not found!")

        except Exception as e:
            print("Error:", e)

    def update_room(self):

        try:

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

        except Exception as e:

            print("Error:", e)

    def search_room(self):

        keyword = input("Keyword: ")

        rooms = self.room_service.search_room(
            keyword
        )

        print("========== SEARCH ROOM RESULT ==========")

        self.print_rooms_table(rooms)

    def sort_room_asc(self):

        rooms = self.room_service.sort_by_price_ascending()

        print("========== SORT ROOM BY PRICE ASC ==========")

        self.print_rooms_table(rooms)

    def sort_room_desc(self):

        rooms = self.room_service.sort_by_price_descending()

        print("========== SORT ROOM BY PRICE DESC ==========")

        self.print_rooms_table(rooms)

    def sort_capacity_asc(self):

        rooms = self.room_service.sort_by_capacity_ascending()

        print("========== SORT ROOM BY CAPACITY ASC ==========")

        self.print_rooms_table(rooms)

    def sort_capacity_desc(self):

        rooms = self.room_service.sort_by_capacity_descending()

        print("========== SORT ROOM BY CAPACITY DESC ==========")

        self.print_rooms_table(rooms)

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

        print("========== CUSTOMER LIST ==========")

        self.print_customers_table(customers)

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

        try:

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

        except Exception as e:

            print("Error:", e)

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

        print("========== SEARCH CUSTOMER RESULT ==========")

        self.print_customers_table(customers)

    # ==================================
    # BOOKING MENU
    # ==================================

    def booking_menu(self):

        while True:

            print("========== BOOKING MANAGEMENT ==========")
            print("1. Create Booking")
            print("2. View Bookings")
            print("3. Update Booking")
            print("4. Cancel Booking")
            print("5. Search Booking By Customer")
            print("6. Sort Booking By Price")
            print("0. Back")

            choice = input("Choose: ")

            if choice == "1":
                self.create_booking()

            elif choice == "2":
                self.view_bookings()

            elif choice == "3":
                self.update_booking()

            elif choice == "4":
                self.cancel_booking()

            elif choice == "5":
                self.search_booking_by_customer()

            elif choice == "6":
                self.sort_booking_by_price()

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

        print("========== BOOKING LIST ==========")

        self.print_bookings_table(bookings)

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

    def update_booking(self):

        try:

            booking_id = input("Booking ID: ")

            customer_id = input(
                "New Customer ID (leave blank to keep old): "
            )

            room_id = input(
                "New Room ID (leave blank to keep old): "
            )

            check_in = input(
                "New Check In (YYYY-MM-DD, leave blank to keep old): "
            )

            check_out = input(
                "New Check Out (YYYY-MM-DD, leave blank to keep old): "
            )

            booking = self.booking_service.update_booking(
                booking_id,
                customer_id if customer_id != "" else None,
                room_id if room_id != "" else None,
                check_in if check_in != "" else None,
                check_out if check_out != "" else None
            )

            print("Booking updated successfully!")
            print(f"Total Price: {booking.total_price}")

        except Exception as e:

            print("Error:", e)

    def search_booking_by_customer(self):

        customer_id = input("Customer ID: ")

        bookings = self.booking_service.find_bookings_by_customer_id(
            customer_id
        )

        print("========== SEARCH BOOKING RESULT ==========")

        self.print_bookings_table(bookings)

    def sort_booking_by_price(self):

        bookings = self.booking_service.sort_bookings_by_total_price(
            descending=True
        )

        print("========== SORT BOOKING BY PRICE DESC ==========")

        self.print_bookings_table(bookings)

    # ==================================
    # REPORT MENU
    # ==================================

    def report_menu(self):

        while True:

            print("========== REPORTS ==========")
            print("1. Total Revenue")
            print("2. Revenue By Room Type")
            print("3. Available Rooms")
            print("4. Booked Rooms")
            print("5. Room Statistics")
            print("6. Top 3 Bookings")
            print("7. Export Booking CSV")
            print("8. Export Revenue CSV")
            print("0. Back")

            choice = input("Choose: ")

            if choice == "1":
                self.show_revenue()

            elif choice == "2":
                self.show_revenue_by_room_type()

            elif choice == "3":
                self.show_available_rooms()

            elif choice == "4":
                self.show_booked_rooms()

            elif choice == "5":
                self.show_room_statistics()

            elif choice == "6":
                self.show_top_bookings()

            elif choice == "7":
                self.export_csv()

            elif choice == "8":
                self.export_revenue_csv()

            elif choice == "0":
                break

            else:
                print("Invalid choice!")

    def show_revenue(self):

        revenue = (
            self.report_service
            .get_total_revenue()
        )

        table = PrettyTable()

        table.field_names = [
            "Report",
            "Value"
        ]

        table.align = "l"

        table.add_row([
            "Total Revenue",
            revenue
        ])

        print(table)

    def show_revenue_by_room_type(self):

        revenue = (
            self.report_service
            .get_revenue_by_room_type()
        )

        print("===== REVENUE BY ROOM TYPE =====")

        self.print_revenue_table(revenue)

    def show_room_statistics(self):

        stats = (
            self.report_service
            .get_room_statistics()
        )

        print("===== ROOM STATISTICS =====")

        self.print_room_statistics_table(stats)

    def show_top_bookings(self):

        bookings = (
            self.report_service
            .get_top_bookings()
        )

        print("===== TOP 3 BOOKINGS =====")

        self.print_bookings_table(bookings)

    def export_revenue_csv(self):

        self.report_service.export_revenue_report_csv()

        print(
            "revenue_report.csv exported successfully!"
        )

    def show_available_rooms(self):

        rooms = (
            self.report_service
            .get_available_rooms()
        )

        print(
            "===== AVAILABLE ROOMS ====="
        )

        self.print_rooms_table(rooms)

    def show_booked_rooms(self):

        rooms = (
            self.report_service
            .get_booked_rooms()
        )

        print(
            "===== BOOKED ROOMS ====="
        )

        self.print_rooms_table(rooms)

    def export_csv(self):

        self.report_service.export_bookings_csv()

        print(
            "booking_report.csv exported successfully!"
        )
