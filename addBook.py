import json
import uuid
from datetime import date

FILE_NAME = "store.json"


class Book:

    def __init__(self, title, author, category, quantity):
        self.id = uuid.uuid4().hex[:11]
        self.title = title
        self.author = author
        self.category = category
        self.quantity = quantity
        self.available = quantity
        self.create_date = str(date.today())

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "category": self.category,
            "quantity": self.quantity,
            "available": self.available,
            "create_date": self.create_date
        }


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_book():

    title = input("Enter Title: ")
    author = input("Enter Author: ")
    category = input("Enter Category: ")
    quantity = int(input("Enter Quantity: "))

    book = Book(title, author, category, quantity)

    books = load_data()

    books.append(book.to_dict())

    save_data(books)

    print("Book Added Successfully!")