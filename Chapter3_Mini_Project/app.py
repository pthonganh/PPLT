import os

def load_data(filename):
    books = []
    if not os.path.exists(filename):
        return books

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 7:
                books.append({
                    "id": parts[0],
                    "title": parts[1],
                    "author": parts[2],
                    "year": int(parts[3]),
                    "quantity": int(parts[4]),
                    "category": parts[5],
                    "status": parts[6]
                })
    return books


def save_data(filename, books):
    with open(filename, "w", encoding="utf-8") as f:
        for b in books:
            f.write(f"{b['id']}|{b['title']}|{b['author']}|{b['year']}|{b['quantity']}|{b['category']}|{b['status']}\n")


def add_book(books):
    print("--- ADD BOOK ---")

    book_id = input("ID: ")
    title = input("Title: ")
    author = input("Author: ")

    while True:
        try:
            year = int(input("Year: "))
            break
        except:
            print("Year must be a number!")

    while True:
        try:
            quantity = int(input("Quantity: "))
            break
        except:
            print("Quantity must be a number!")

    category = input("Category: ")
    status = input("Status (Available/Borrowed): ")

    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "year": year,
        "quantity": quantity,
        "category": category,
        "status": status
    })

    print("Added successfully!")

def display_books(books):
    if not books:
        print("No books found.")
        return

    headers = ["ID", "Title", "Author", "Year", "Qty", "Category", "Status"]

    rows = []
    for b in books:
        rows.append([
            str(b["id"]),
            str(b["title"]),
            str(b["author"]),
            str(b["year"]),
            str(b["quantity"]),
            str(b["category"]),
            str(b["status"])
        ])

    col_widths = []
    for i in range(len(headers)):
        max_width = len(headers[i])
        for row in rows:
            if len(row[i]) > max_width:
                max_width = len(row[i])
        col_widths.append(max_width)

    def print_border():
        print("+" + "+".join("-" * (w + 2) for w in col_widths) + "+")

    def print_row(row):
        print("| " + " | ".join(row[i].ljust(col_widths[i]) for i in range(len(row))) + " |")

    print()
    print_border()
    print_row(headers)
    print_border()

    for row in rows:
        print_row(row)

    print_border()


def search_book(books):
    if not books:
        print("No books found.")
        return

    print("--- SEARCH OPTIONS ---")
    print("1. Search by ID")
    print("2. Search by Title keyword")
    print("3. Search by Year")
    print("4. Search by Author")
    print("5. Search by Category")

    choice = input("Choose: ").strip()
    results = []

    if choice == "1":
        keyword = input("Enter book ID: ").strip().lower()
        for b in books:
            if str(b["id"]).lower() == keyword:
                results.append(b)

    elif choice == "2":
        keyword = input("Enter title keyword: ").strip().lower()
        for b in books:
            if keyword in str(b["title"]).lower():
                results.append(b)

    elif choice == "3":
        year = input("Enter year: ").strip()
        for b in books:
            if str(b["year"]) == year:
                results.append(b)

    elif choice == "4":
        keyword = input("Enter author name: ").strip().lower()
        for b in books:
            if keyword in str(b["author"]).lower():
                results.append(b)

    elif choice == "5":
        keyword = input("Enter category: ").strip().lower()
        for b in books:
            if keyword in str(b["category"]).lower():
                results.append(b)

    else:
        print("Invalid choice!")
        return

    if results:
        print("Search results:")
        display_books(results)
    else:
        print("No matching books found.")

def sort_books(books):
    if not books:
        print("No books to sort.")
        return

    print("--- SORT OPTIONS ---")
    print("1. Sort by Title (A-Z)")
    print("2. Sort by Year")
    print("3. Sort by Quantity")

    choice = input("Choose: ")

    if choice == "1":
        books.sort(key=lambda x: x["title"].lower())
        print("Sorted by Title (A-Z)")

    elif choice == "2":
        books.sort(key=lambda x: x["year"])
        print("Sorted by Year")

    elif choice == "3":
        books.sort(key=lambda x: x["quantity"])
        print("Sorted by Quantity")

    else:
        print("Invalid choice!")
        return
    
    display_books(books)


def statistics(books):
    if not books:
        print("No data.")
        return

    total = len(books)
    total_qty = sum(b["quantity"] for b in books)

    print("--- STATISTICS ---")
    print("Total titles:", total)
    print("Total quantity:", total_qty)

def display_menu():
    print("===== FAMILY LIBRARY MANAGEMENT =====")
    print("1. Add book")
    print("2. Display books")
    print("3. Search book")
    print("4. Sort books")
    print("5. Statistics")
    print("0. Exit")

def main():
    file = "Chapter3_Mini_Project/books.txt"
    books = load_data(file)

    while True:
        display_menu()
        choice = input("Choose: ")

        if choice == "1":
            add_book(books)

        elif choice == "2":
            display_books(books)

        elif choice == "3":
            search_book(books)

        elif choice == "4":
            sort_books(books)

        elif choice == "5":
            statistics(books)

        elif choice == "0":
            save_data(file, books)
            print("Saved. Exit.")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

