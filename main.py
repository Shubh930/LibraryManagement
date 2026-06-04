from Domain.addBook import add_book
from Domain.viewBook import view_books
from Domain.updateBook import update_book
from Domain.deleteBook import delete_book

while True:
    print("\n========================")
    print("Library Management System")
    print("========================")
    print("1. Add Book")
    print("2. View Book")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        update_book()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")

    
    
    
