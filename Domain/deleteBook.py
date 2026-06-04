import json

FILE_NAME = "store.json"


def delete_book():

    try:
        with open(FILE_NAME, "r") as file:
            books = json.load(file)

        book_id = input("Enter Book ID to Delete: ")

        new_books = []

        found = False

        for book in books:

            if book["id"] == book_id:
                found = True

            else:
                new_books.append(book)

        if found:

            with open(FILE_NAME, "w") as file:
                json.dump(new_books, file, indent=4)

            print("Book Deleted Successfully!")

        else:
            print("Book Not Found")

    except FileNotFoundError:
        print("No Data Found")