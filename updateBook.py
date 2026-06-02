import json

FILE_NAME = "store.json"


def update_book():

    try:
        with open(FILE_NAME, "r") as file:
            books = json.load(file)

        book_id = input("Enter Book ID to Update: ")

        found = False

        for book in books:

            if book["id"] == book_id:

                found = True

                book["title"] = input("Enter New Title: ")
                book["author"] = input("Enter New Author: ")
                book["category"] = input("Enter New Category: ")

                quantity = int(input("Enter New Quantity: "))

                book["quantity"] = quantity
                book["available"] = quantity

                break

        if found:

            with open(FILE_NAME, "w") as file:
                json.dump(books, file, indent=4)

            print("Book Updated Successfully!")

        else:
            print("Book Not Found")

    except FileNotFoundError:
        print("No Data Found")