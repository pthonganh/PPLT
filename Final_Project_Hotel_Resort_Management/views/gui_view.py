import tkinter as tk
from tkinter import ttk, messagebox


class GUIView:

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

        self.window = tk.Tk()
        self.window.title("Hotel Resort Management System")
        self.window.geometry("1200x700")
        self.window.configure(bg="#f4f7fb")

    def run(self):
        self.create_layout()
        self.show_dashboard()
        self.window.mainloop()

    def create_layout(self):
        self.sidebar = tk.Frame(
            self.window,
            bg="#1f4e79",
            width=230
        )
        self.sidebar.pack(side="left", fill="y")

        self.main_frame = tk.Frame(
            self.window,
            bg="#f4f7fb"
        )
        self.main_frame.pack(side="right", fill="both", expand=True)

        logo = tk.Label(
            self.sidebar,
            text="🏨\nHotel Resort",
            bg="#1f4e79",
            fg="white",
            font=("Arial", 20, "bold")
        )
        logo.pack(pady=30)

        self.add_sidebar_button("Dashboard", self.show_dashboard)
        self.add_sidebar_button("View Rooms", self.show_rooms)
        self.add_sidebar_button("View Customers", self.show_customers)
        self.add_sidebar_button("View Bookings", self.show_bookings)
        self.add_sidebar_button("Revenue Report", self.show_revenue_by_room_type)
        self.add_sidebar_button("Export Booking CSV", self.export_booking_csv)
        self.add_sidebar_button("Export Revenue CSV", self.export_revenue_csv)

        exit_button = tk.Button(
            self.sidebar,
            text="Exit",
            bg="#d9534f",
            fg="white",
            activebackground="#c9302c",
            activeforeground="white",
            font=("Arial", 12, "bold"),
            relief="flat",
            command=self.window.destroy
        )
        exit_button.pack(
            side="bottom",
            fill="x",
            padx=20,
            pady=30
        )

        header = tk.Frame(
            self.main_frame,
            bg="#f4f7fb"
        )
        header.pack(fill="x", padx=30, pady=20)

        tk.Label(
            header,
            text="Hotel Resort Management System",
            bg="#f4f7fb",
            fg="#1f2937",
            font=("Arial", 26, "bold")
        ).pack(anchor="w")

        tk.Label(
            header,
            text="Manage rooms, customers, bookings and reports",
            bg="#f4f7fb",
            fg="#6b7280",
            font=("Arial", 12)
        ).pack(anchor="w", pady=5)

        self.content = tk.Frame(
            self.main_frame,
            bg="#f4f7fb"
        )
        self.content.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=10
        )

    def add_sidebar_button(self, text, command):
        button = tk.Button(
            self.sidebar,
            text=text,
            bg="#1f4e79",
            fg="white",
            activebackground="#2563eb",
            activeforeground="white",
            font=("Arial", 12),
            relief="flat",
            anchor="w",
            padx=25,
            pady=12,
            command=command
        )
        button.pack(
            fill="x",
            padx=10,
            pady=3
        )

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def create_card(self, parent, title, value, color):
        card = tk.Frame(
            parent,
            bg="white",
            relief="groove",
            bd=1
        )
        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        tk.Label(
            card,
            text=title,
            bg="white",
            fg="#6b7280",
            font=("Arial", 12)
        ).pack(pady=(18, 5))

        tk.Label(
            card,
            text=value,
            bg="white",
            fg=color,
            font=("Arial", 22, "bold")
        ).pack(pady=(0, 18))

    def show_dashboard(self):
        self.clear_content()

        card_frame = tk.Frame(
            self.content,
            bg="#f4f7fb"
        )
        card_frame.pack(fill="x")

        total_rooms = len(self.room_service.get_all_rooms())
        total_customers = len(self.customer_service.get_all_customers())
        total_bookings = len(self.booking_service.get_all_bookings())
        total_revenue = self.report_service.get_total_revenue()

        self.create_card(card_frame, "Total Rooms", total_rooms, "#2563eb")
        self.create_card(card_frame, "Total Customers", total_customers, "#16a34a")
        self.create_card(card_frame, "Total Bookings", total_bookings, "#f97316")
        self.create_card(card_frame, "Total Revenue", total_revenue, "#9333ea")

        button_frame = tk.Frame(
            self.content,
            bg="#f4f7fb"
        )
        button_frame.pack(pady=20)

        tk.Button(
            button_frame,
            text="Refresh Dashboard",
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            padx=20,
            pady=8,
            command=self.show_dashboard
        ).pack()

        info = tk.Label(
            self.content,
            text="Welcome to Hotel Resort Management System",
            bg="#f4f7fb",
            fg="#374151",
            font=("Arial", 14)
        )
        info.pack(pady=20)

    def create_table(self, columns):
        table_frame = tk.Frame(
            self.content,
            bg="white",
            relief="groove",
            bd=1
        )
        table_frame.pack(
            fill="both",
            expand=True,
            pady=10
        )

        tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        for column in columns:
            tree.heading(column, text=column)
            tree.column(column, width=150, anchor="center")

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=tree.yview
        )
        tree.configure(yscrollcommand=scrollbar.set)

        tree.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(10, 0),
            pady=10
        )

        scrollbar.pack(
            side="right",
            fill="y",
            pady=10,
            padx=(0, 10)
        )

        return tree

    def create_section_title(self, title):
        tk.Label(
            self.content,
            text=title,
            bg="#f4f7fb",
            fg="#1f2937",
            font=("Arial", 18, "bold")
        ).pack(anchor="w", pady=10)

    def show_rooms(self):
        self.clear_content()
        self.create_section_title("Room List")

        columns = (
            "Room ID",
            "Type",
            "Price",
            "Capacity",
            "Status",
            "Services"
        )

        tree = self.create_table(columns)

        for room in self.room_service.get_all_rooms():
            tree.insert(
                "",
                "end",
                values=(
                    room.room_id,
                    room.get_room_type(),
                    room.price,
                    room.capacity,
                    room.status,
                    ", ".join(room.get_services())
                )
            )

    def show_customers(self):
        self.clear_content()
        self.create_section_title("Customer List")

        columns = (
            "Customer ID",
            "Name",
            "Phone",
            "Email"
        )

        tree = self.create_table(columns)

        for customer in self.customer_service.get_all_customers():
            tree.insert(
                "",
                "end",
                values=(
                    customer.customer_id,
                    customer.name,
                    customer.phone,
                    customer.email
                )
            )

    def show_bookings(self):
        self.clear_content()
        self.create_section_title("Booking List")

        columns = (
            "Booking ID",
            "Customer ID",
            "Room ID",
            "Check In",
            "Check Out",
            "Total Price"
        )

        tree = self.create_table(columns)

        for booking in self.booking_service.get_all_bookings():
            tree.insert(
                "",
                "end",
                values=(
                    booking.booking_id,
                    booking.customer_id,
                    booking.room_id,
                    booking.check_in,
                    booking.check_out,
                    booking.total_price
                )
            )

    def show_revenue_by_room_type(self):
        self.clear_content()
        self.create_section_title("Revenue By Room Type")

        columns = (
            "Room Type",
            "Revenue"
        )

        tree = self.create_table(columns)

        revenue_data = self.report_service.get_revenue_by_room_type()

        for room_type, revenue in revenue_data.items():
            tree.insert(
                "",
                "end",
                values=(
                    room_type,
                    revenue
                )
            )

    def export_booking_csv(self):
        self.report_service.export_bookings_csv()

        messagebox.showinfo(
            "Export Success",
            "Booking report has been exported successfully."
        )

    def export_revenue_csv(self):
        self.report_service.export_revenue_report_csv()

        messagebox.showinfo(
            "Export Success",
            "Revenue report has been exported successfully."
        )