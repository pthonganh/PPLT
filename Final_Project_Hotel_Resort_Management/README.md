# HOTEL RESORT MANAGEMENT SYSTEM

## 1. Project Description

Hotel Resort Management System is a Python application developed using Object-Oriented Programming (OOP) principles.

The system helps hotel staff manage:

* Rooms
* Customers
* Bookings
* Revenue Reports

The application follows a Layered Architecture and supports both CLI (Command Line Interface) and GUI (Tkinter) interfaces.

This project applies the concepts learned in Programming Methods:

* Object-Oriented Programming (OOP)
* Encapsulation
* Inheritance
* Polymorphism
* Abstraction
* Layered Architecture
* CRUD Operations
* Search & Sort
* JSON File Handling
* Statistics & Reporting
* GUI Development
* Git & GitHub Version Control

---

## 2. Project Objectives

The system is developed with the following objectives:

* Manage hotel rooms efficiently
* Manage customer information
* Create and cancel bookings
* Generate revenue reports
* Export report data to CSV files
* Store data permanently using JSON files
* Demonstrate OOP principles and software architecture

---

## 3. Technologies Used

| Component    | Role                      |
| ------------ | ------------------------- |
| Python       | Main Programming Language |
| JSON         | Permanent Data Storage    |
| CSV          | Report Export             |
| Tkinter      | GUI Interface             |
| CLI          | Command Line Interface    |
| Git & GitHub | Version Control           |

---

## 4. Project Structure

```text
Hotel_Resort_Management/
│
├── data/
│   ├── rooms.json
│   ├── customers.json
│   └── bookings.json
│
├── models/
│   ├── room.py
│   ├── standard_room.py
│   ├── vip_room.py
│   ├── villa_room.py
│   ├── customer.py
│   └── booking.py
│
├── services/
│   ├── room_service.py
│   ├── customer_service.py
│   ├── booking_service.py
│   └── report_service.py
│
├── views/
│   ├── menu_view.py
│   └── gui_view.py
│
├── main.py
├── booking_report.csv
├── revenue_report.csv
└── README.md
```

---

## 5. OOP Concepts Applied

### Encapsulation

Sensitive attributes are private and accessed through Property Getter/Setter.

Examples:

```python
self.__price
self.__capacity
self.__status
```

Validation is performed in setters.

---

### Inheritance

Room is the parent class.

Child classes:

* StandardRoom
* VIPRoom
* VillaRoom

```text
Room
├── StandardRoom
├── VIPRoom
└── VillaRoom
```

---

### Polymorphism

Child classes override methods:

```python
calculate_price()
get_room_type()
get_services()
```

Each room type provides different behavior.

---

### Abstraction

The Room class is implemented as an Abstract Base Class (ABC).

```python
class Room(ABC):
```

Mandatory methods:

```python
@abstractmethod
def calculate_price(self, days):
```

```python
@abstractmethod
def get_room_type(self):
```

```python
@abstractmethod
def get_services(self):
```

---

## 6. Main Features

### Room Management

* Add Room
* View Rooms
* Update Room
* Delete Room
* Search Room
* Sort Rooms

### Customer Management

* Add Customer
* View Customers
* Update Customer
* Delete Customer
* Search Customer
* Sort Customers

### Booking Management

* Create Booking
* View Bookings
* Update Booking
* Cancel Booking

### Reports

* Total Revenue
* Revenue By Room Type
* Available Rooms
* Booked Rooms
* Room Statistics
* Top 3 Bookings
* Export Booking CSV
* Export Revenue CSV

---

## 7. CRUD Operations

The system supports full CRUD operations:

### Room CRUD

* Create Room
* Read Room List
* Update Room
* Delete Room

### Customer CRUD

* Create Customer
* Read Customer List
* Update Customer
* Delete Customer

### Booking CRUD

* Create Booking
* Read Booking List
* Update Booking
* Cancel Booking

---

## 8. Search & Sort

### Search

* Search Room by ID
* Search Customer by Name
* Search Booking by ID

### Sort

* Sort Rooms by Price
* Sort Rooms by Capacity
* Sort Customers by Name
* Sort Bookings by Total Price

---

## 9. Permanent Storage (File I/O)

The application automatically saves and loads data using JSON files.

Files:

* rooms.json
* customers.json
* bookings.json

Data remains available after restarting the application.

---

## 10. Complex Transaction Logic

### Create Booking

The system automatically:

1. Validates Booking ID
2. Validates Customer
3. Validates Room
4. Checks Room Availability
5. Calculates Number of Days
6. Calculates Total Price
7. Creates Booking
8. Updates Room Status
9. Saves Data

### Cancel Booking

The system automatically:

1. Finds Booking
2. Restores Room Status
3. Removes Booking
4. Saves Data

---

## 11. Advanced Statistics & Export

### Statistics

The system provides:

* Total Revenue
* Revenue By Room Type
* Room Statistics
* Top 3 Bookings

### Export

Supported exports:

* booking_report.csv
* revenue_report.csv

These files can be opened using Microsoft Excel or Google Sheets.

---

## 12. Advanced Technology

The project includes a Graphical User Interface (GUI) developed using Tkinter.

Features:

* View Rooms
* View Customers
* View Bookings
* Revenue Reports
* CSV Export

The system also supports CLI mode.

---

## 13. Evaluation Criteria Mapping

| Evaluation Criteria  | Implementation                                              |
| -------------------- | ----------------------------------------------------------- |
| Encapsulation        | Private attributes with Getter/Setter                       |
| Inheritance          | Room → StandardRoom, VIPRoom, VillaRoom                     |
| Polymorphism         | Override calculate_price(), get_room_type(), get_services() |
| Abstraction          | Room(ABC) and @abstractmethod                               |
| Layered Architecture | models/, services/, views/                                  |
| Clean Code           | CamelCase & snake_case naming                               |
| Exception Handling   | try-except and input validation                             |
| CRUD                 | RoomService, CustomerService, BookingService                |
| Search & Sort        | Search and sorting functions                                |
| Permanent Storage    | JSON File Handling                                          |
| Transaction Logic    | Create Booking & Cancel Booking                             |
| Statistics & Export  | Revenue Reports & CSV Export                                |
| Advanced Technology  | Tkinter GUI                                                 |
| Git & GitHub         | Public Repository & Commit History                          |

---

## 14. Self Assessment

| #  | Component                  | Score |
| -- | -------------------------- | ----- |
| 1  | Encapsulation              | 0.5   |
| 2  | Inheritance                | 0.5   |
| 3  | Polymorphism & Abstraction | 1.0   |
| 4  | Layered Architecture       | 1.0   |
| 5  | Clean Code                 | 0.5   |
| 6  | Exception Handling         | 0.5   |
| 7  | CRUD                       | 1.0   |
| 8  | Search & Sort              | 1.0   |
| 9  | Permanent Storage          | 1.0   |
| 10 | Complex Transaction Logic  | 1.0   |
| 11 | Statistics & Export        | 1.0   |
| 12 | GUI                        | 0.5   |
| 13 | Git & GitHub               | 0.5   |

TOTAL: 10.0 / 10.0

---

## 15. How To Run

### Step 1

Open the project folder in VS Code.

### Step 2

Open Terminal.

### Step 3

Run:

```bash
python main.py
```

### Step 4

Choose:

```text
1. CLI
2. GUI
```

---

## 16. Student Information

Name: ....................................

Student ID: ..............................

Class: ...................................

Course: Programming Methods

---

## 17. Conclusion

This project successfully satisfies all requirements of the Final Project.

The system applies OOP principles, Layered Architecture, CRUD operations, Search & Sort, Permanent Storage, Complex Transaction Logic, Statistics & Export, GUI development, and GitHub version control.

The project is modular, maintainable, and demonstrates practical software development skills using Python.
