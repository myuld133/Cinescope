# проект библиотека
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_books.append(book.title)
        else:
            print(f"Книга '{book.title}' уже занята.")

    def return_book(self, book):
        if book.title in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.title)

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            status = "Занята" if book.is_borrowed else "Свободна"
            print(f"{book.title} ({book.author}) - {status}")

book1 = Book('Мастер и Маргарита', 'Булгаков М.А.')
user1 = User('Ann')
user1.borrow_book(book1)
print(user1.borrowed_books)