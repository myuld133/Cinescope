# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     @property  # Декоратор для геттера name
#     def name(self):
#         return self._name
#
#     @name.setter  # Декоратор для сеттера name
#     def name(self, new_name):
#         self._name = new_name
#
#     @property  # Декоратор для геттера age
#     def age(self):
#         return self._age
#
#     @age.setter  # Декоратор для сеттера age
#     def age(self, new_age):
#         if new_age < 0: # Проверка значения (возраст не может быть отрицательным)
#             print("Возраст должен быть неотрицательным!")
#         else:
#             self._age = new_age
#
# # Создаем объект
# person = Person("Петр", 30)
#
# """Обращаемся к атрибутам как к обычным переменным"""
# person.age = -5  # Вывод: Возраст должен быть неотрицательным!
#
# """Теперь передадим положительное значение"""
# person.age = 35
# print(person.age) #вывод 35



# class Circle:
#     def __init__(self, radius):
#         self._radius = radius
#
#     @property
#     def radius(self):
#         return self._radius
#
#     @radius.setter
#     def radius(self, new_radius):
#         if new_radius < 0:
#             print("Радиус не может быть отрицательным.")
#         else:
#             self._radius = new_radius
#
#     @property
#     def area(self):  # Вычисляемое свойство (площадь круга)
#         return 3.14159 * self._radius**2
#
# circle = Circle(5)
# print(circle.area)  # Вывод: 78.53975
# circle.radius = 10
# print(circle.area) #вывод 314.159
# circle.radius = -5
# print(circle.area) #вывод 314.159


class Book:
    def __init__(self, title, author, pages):
        self._title1 = title
        self._author = author
        self._pages = pages

    @property
    def p_title(self):
        return self._title1

    @p_title.setter
    def p_title(self, new_title):
        self._title1 = new_title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        self._author = new_author

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages):
        if new_pages <= 0:
            print('Количество страниц не должно быть отрицательным')
        else:
            self._pages = new_pages

book = Book('Мастер и Маргарита', 'Михаил Булгаков', 384)
print(book.p_title)
print(book.author)
print(book.pages)
book.pages = 500
print(book.pages)
book.pages = -10


# class BankAccount:
#     def __init__(self, account_number, balance):
#         self._account_number = account_number
#         self._balance = balance
#
#     @property
#     def balance(self):
#         return self._balance
#
#     @balance.setter
#     def balance(self, new_balance):
#         if new_balance < self._balance:
#             print('Операция снятия средств не поддерживается. Используйте метод withdraw()')
#         else:
#             self._balance = new_balance
#
#     def withdraw(self, amount):
#         if 0 <= amount <= self._balance:
#             self._balance -= amount
#         else:
#             print('Некорректная сумма для списания')
#
# acc1 = BankAccount(123, 7000)
# print(acc1.balance)
# acc1.balance = 5000
# print(acc1.balance)
# acc1.withdraw(2000)
# print(acc1.balance)
# acc1.withdraw(10000)
# print(acc1.balance)