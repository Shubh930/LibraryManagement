import json

FILE_NAME = r"C:\Users\shubhendra singh\OneDrive\Desktop\python\LibraryManagement\Database\store.json"


def view_books():

    try:
        with open(FILE_NAME, "r") as file:
            books = json.load(file)

        if len(books) == 0:
            print("No Books Available")
            return

        for book in books:

            print("\n----------------------")
            print("ID :", book["id"])
            print("Title :", book["title"])
            print("Author :", book["author"])
            print("Category :", book["category"])
            print("Quantity :", book["quantity"])
            print("Available :", book["available"])
            print("Create Date :", book["create_date"])

    except FileNotFoundError:
        print("No Data Found")