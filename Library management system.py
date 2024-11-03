books = ["Harry Potter", "The Hobbit", "Pride and Prejudice"]
issued_books = {}-

def display_books():
    print("Available books:")
    for book in books:
        print(f"- {book}")

def issue_book(book, user):
    if book in books:
        books.remove(book)
        issued_books[book] = user
        print(f"Issued '{book}' to {user}.")
    else:
        print(f"'{book}' is not available.")

def return_book(book):
    if book in issued_books:
        user = issued_books.pop(book)
        books.append(book)
        print(f"'{book}' returned by {user}.")
    else:
        print(f"No record of '{book}' being issued.")

while True:-
    print("\n1. Display Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        display_books()
    elif choice == '2':
        book = input("Enter book name to issue: ")
        user = input("Enter your name: ")
        issue_book(book, user)
    elif choice == '3':
        book = input("Enter book name to return: ")
        return_book(book)
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
