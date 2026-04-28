# MINI PROJECT 3 - FAMILY LIBRARY MANAGEMENT

## 1. Project Description
This is a Python console application for managing a family library, built using procedural programming methods.

The program runs on a CLI (Command Line Interface) environment, allowing users to interact through a menu. The system supports managing books, including adding, displaying, searching, sorting, calculating statistics, saving data, and exporting/importing data.

This project applies knowledge from Programming Methods 1:
- Using functions to divide the program into smaller parts
- Using loops to build an interactive menu (while True)
- Using conditional statements to handle user choices
- Using lists and dictionaries to manage data
- Validating user input
- Reading and writing files (TXT, JSON)
- Displaying data in formatted tables

Selected Topic: Topic 1 - Family Library Management

---

## 2. Project Objective
The system is built with the following objectives:
- Manage books effectively and simply
- Allow users to add, view, search, and sort books
- Provide statistics about the library
- Save and reload data automatically
- Export and import structured data using JSON
- Practice procedural programming and modular design

---

## 3. Data Structure
Each book is stored as a dictionary:

```python
{
    "id": "B001",
    "title": "Python Basics",
    "author": "John",
    "year": 2023,
    "quantity": 10,
    "category": "IT",
    "status": "Available"
}
```

All books are stored in a list:

```python
books = [
    {
        "id": "B001",
        "title": "Python Basics",
        "author": "John",
        "year": 2023,
        "quantity": 10,
        "category": "IT",
        "status": "Available"
    }
]
```

This structure allows easy operations such as add, search, sort, and statistics.

---

## 4. Technologies Used
| Component | Role |
|----------|------|
| Python | Main programming language |
| TXT File | Persistent storage |
| JSON File | Structured data storage |
| Git & GitHub | Version control |
| CLI | User interaction |

---

## 5. Project Structure
```text
Chapter3_Mini_Project/
├── app.py
├── books.txt
├── books.json
└── README.md
```

---

## 6. Main Features

### Add Book
Users can input:
- Book ID
- Title
- Author
- Year
- Quantity
- Category
- Status

The program validates numeric fields (year, quantity).

---

### Display Books
Displays all books in a formatted table with aligned columns:
- ID
- Title
- Author
- Year
- Quantity
- Category
- Status

---

### Search Books
Supports:
- Search by ID (exact match)
- Search by title keyword (partial match)
- Search by author
- Search by category
- Search by year

---

### Sort Books
Sort data by:
- Title (A–Z)
- Year
- Quantity

---

### Statistics
Calculates:
- Total number of book titles
- Total quantity of books

---

### TXT File Handling
- Load data from `books.txt` when program starts
- Save data when exiting (option 0)
- Prevent data loss

---

### JSON Import / Export
- Export to `books.json`
- Import from `books.json`
- Support structured data storage

---

## 7. Menu
```text
===== FAMILY LIBRARY MANAGEMENT =====
1. Add book
2. Display books
3. Search book
4. Sort books
5. Statistics
6. Export to JSON
7. Load from JSON
0. Exit
```

---

## 8. Input Validation
- Year must be a number
- Quantity must be a number
- ID cannot be empty

---

## 9. Main Functions
- load_data(): load data from TXT file
- save_data(): save data to TXT file
- add_book(): add a new book
- display_books(): display table
- search_book(): search books
- sort_books(): sort books
- statistics(): calculate data
- export_json(): export JSON
- import_json(): import JSON
- display_menu(): show menu
- main(): control program

---

## 10. Advanced Features
- Keyword search (partial match)
- JSON import/export

---

## 11. How to Run
Step 1: Open Project Folder

Open the folder Chapter3_Mini_Project in VS Code.

Step 2: Open Terminal or CMD

Make sure you are inside the project folder.

Step 3: Run the Program
```bash
python app.py
```

---

## 12. Usage Example

Add Book:
```
ID: B001
Title: Python Basics
Author: John
Year: 2023
Quantity: 10
Category: IT
Status: Available
```

Display:
```
+------+---------------+--------+------+-----+----------+-----------+
| ID   | Title         | Author | Year | Qty | Category | Status    |
+------+---------------+--------+------+-----+----------+-----------+
| B001 | Python Basics | John   | 2023 | 10  | IT       | Available |
+------+---------------+--------+------+-----+----------+-----------+
```

---

## 13. Self Assessment
| # | Component | Score |
|---|----------|------|
| 1 | CLI Menu | 1.0 |
| 2 | Input Validation | 1.0 |
| 3 | Display | 1.0 |
| 4 | Search | 1.0 |
| 5 | Sort | 1.0 |
| 6 | Statistics | 1.0 |
| 7 | TXT File | 1.0 |
| 8 | Advanced Search | 1.0 |
| 9 | JSON | 1.0 |
| 10 | Git & README | 1.0 |

TOTAL: 10.0 / 10.0

---

## 14. Student Information
Name: Phan Trần Hồng Anh  
Student ID: 24S7040002  
Class: Tin2E  
Course: Programming Methods 1  

---

## 15. Conclusion
This project satisfies the requirements of the mini project.

It uses a CLI menu, functions, loops, conditional statements, input validation, TXT file handling, JSON file handling, searching, sorting, and statistics.

The program is organized using procedural programming, making it clear, modular, and easy to understand.