# # создание класса
# class Human:
#     pass
#
# human1 = Human() # создание объекта класса Human
# human2 = Human()
#
#
# # работа с атрибутами объекта
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
# book1 = Book('Война и мир', 'Л.Н. Толстой', 2144) # создание объекта класса Book
#
# print(book1.title)
# print(book1.author)
# print(book1.pages)
#
# book1.title = 'Война и мир 2 том' # изменение атрибута конкретного объекта
# print(book1.title)
#
# book1.genre = 'Русская классика' # добавление нового атрибута объекту
# print(book1.genre)
#
#
# # атрибуты класса
# class Employee:
#     company_name = "TechCorp"  # Атрибут класса
#
#     def __init__(self, name, position):
#         self.name = name  # Атрибут объекта
#         self.position = position  # Атрибут объекта
#
#     def display_info(self):
#         print(f"{self.name} works as a {self.position} at {Employee.company_name}.")
#
#
# # Создание объектов класса Employee
# emp1 = Employee("Alice", "Developer")
# emp2 = Employee("Bob", "Designer")
#
# emp1.display_info()  # Вывод: Alice works as a Developer at TechCorp.
# emp2.display_info()  # Вывод: Bob works as a Designer at TechCorp.
#
# # Изменение атрибута класса
# Employee.company_name = "DevSolutions"
# emp1.display_info()  # Вывод: Alice works as a Developer at DevSolutions.
from os import access


# методы классов
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def speak(self):
#         print(f'I am an animal, my name is {self.name} and my age is {self.age}.')
#
# cat = Animal('Goshka', 5)
# cat.speak()
#
# cat.name = 'Murka'
# cat.age = 2
# cat.speak()


# анализ введенных чисел
# class Analyze:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def biggest(self):
#         max_num = max(self.a, self.b)
#         return max_num
#
#     def even(self):
#         max_num = self.biggest()
#         if max_num % 2 == 0:
#             print('четное число')
#         else:
#             print('нечетное число')
#
#     def positive_or_negative(self):
#         max_num = self.biggest()
#         if max_num > 0:
#             print('положительное число')
#         elif self.a < 0:
#             print('отрицательное число')
#         else:
#             print('равен нулю')
#
#
# numbers1 = Analyze(3,2)
# print(numbers1.biggest())
# numbers1.even()
# numbers1.positive_or_negative()


# наследование классов - родительский и дочерний

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        assert self.balance > 0, f'ValueError'

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        assert amount > 0, f'Negative amount'
        if self.balance > amount:
            self.balance -= amount
        else:
            self.balance = 0

class SavingsAccount(Account):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        assert (self.balance - amount) >= 100, f'Минимальный остаток должен быть 100'
        super().withdraw(amount)

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.deposit(interest)


# acc1 = Account('Yulka', 20)
# acc1.deposit(10)
# acc1.withdraw(-40)
# print(acc1.balance)

# acc2 = SavingsAccount('Goshka', 200, 20)
# acc2.withdraw(50)
# print(acc2.balance)


class Person:
    some_num = 123 # атрибут класса = статический атрибут
    counter = 0

    def __init__(self, name, surname, place_of_birth, year_of_birth):
        self.name = name
        self.surname = surname
        self.place_of_birth = place_of_birth
        self.year_of_birth = year_of_birth
        Person.counter += 1

    def print_info(self):
        print(f'Name: {self.name}, Surname: {self.surname}, Place_of_birth: {self.place_of_birth}, Year_of_birth: {self.year_of_birth}')

    def get_age(self, current_year):
        return current_year - self.year_of_birth

p1 = Person('Yulka', 'Timofeeva', 'Kazan', 2000)
p2 = Person('Pashka', 'Timofeev', 'SPB', 1999)
p3 = Person('Goshka', 'Maksimov', 'SPB', 2020)

print(Person.counter)