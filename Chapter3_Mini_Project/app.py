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

    print("\n{:<6} {:<15} {:<15} {:<8} {:<6} {:<12} {:<10}".format(
        "ID", "Title", "Author", "Year", "Qty", "Category", "Status"
    ))
    print("-" * 75)

    for b in books:
        print("{:<6} {:<15} {:<15} {:<8} {:<6} {:<12} {:<10}".format(
            b["id"],
            b["title"],
            b["author"],
            b["year"],
            b["quantity"],
            b["category"],
            b["status"]
        ))


def display_menu():
    print("===== FAMILY LIBRARY MANAGEMENT =====")
    print("1. Add book")
    print("2. Display books")
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

        elif choice == "0":
            save_data(file, books)
            print("Saved. Exit.")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

