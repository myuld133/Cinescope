# # инкапсуляция
#
# # class Safe:
# #     def __init__(self, code, balance):
# #         self.__code = code  # Приватный код
# #         self.__balance = balance  # Приватный баланс
# #
# #     def check_balance(self, code):
# #         if code == self.__code:
# #             return f"Баланс в сейфе: {self.__balance} золотых"
# #         else:
# #             return "Неверный код. Доступ запрещён."
# #
# # # Создаём сейф
# # safe = Safe("1234", 1000)
# #
# # # Попробуем проверить баланс
# # print(safe.check_balance("1234"))  # Баланс в сейфе: 1000 золотых
# # print(safe.check_balance("0000"))  # Неверный код. Доступ запрещён.
#
#
#
# # # protected arguments
# # class BankAccount:
# #     def __init__(self, balance):
# #         self._balance = balance # пометили как protected
# #
# #     def deposit(self, amount):
# #         if amount > 0:
# #             self._balance += amount
# #         else:
# #             print('Сумма депозита должна быть положительной')
# #
# #     def withdraw(self, amount):
# #         if 0 < amount <= self._balance:
# #             self._balance -= amount
# #         else:
# #             print('Недостаточно средств или некорректная сумма')
# #
# #     def get_balance(self):
# #         return self._balance
# #
# #
# # account1 = BankAccount(1000)
# # account1.deposit(500)
# # account1.withdraw(2000)
# # print(account1.get_balance())
# #
# # """Мы можем обратиться к защищенному атрибуту напрямую, но это не рекомендуется"""
# # print(account1._balance)  # Вывод: 1500 (но лучше использовать account.get_balance())
# #
# # account1._balance = -1000 #можем изменить напрямую, но это плохо
# # print(account1.get_balance()) #вывод -1000, что недопустимо
# # account1.withdraw(100)
# # print(account1.get_balance()) #вывод недопустимый
#
#
# class Person:
#
#     def __init__(self, name, age):
#         self._name = name  # _ показывает, что атрибут "внутренний"
#         self._age = None
#         self.__check_and_set_age(age)
#
#
#     def __check_and_set_age(self, age):
#         if age < 0:  # Проверка значения (возраст не может быть отрицательным)
#             print("Возраст должен быть неотрицательным!")
#         else:
#             self._age = age
#
#
#     def get_name(self):
#         return self._name
#
#     def set_name(self, new_name):
#         self._name = new_name
#
#     def get_age(self):
#         return self._age
#
#     def set_age(self, new_age):
#         self.__check_and_set_age(new_age)
#
#
# """Создаем объект класса Person"""
# person = Person("Иван", 30)
# print(person.get_name())
# print(person.get_age())
# person.set_age(-5)
#
# """Используем сеттеры для установки значений (с частичной проверкой)"""
# person.set_age(-10)  # Вывод: Возраст должен быть неотрицательным!
#
# """Используем геттер для получения значения"""
# print(person.get_name())  # Вывод: Иван
# print(person.get_age())
#
# person.set_name("Алексей")
# print(person.get_name()) #вывод Алексей
# person.set_age(30)
# print(person.get_age()) #вывод 30
#
# person2 = Person("Mishka", -5)
# print(person2.get_age())
# person2.set_age(10)
# print(person2.get_age())


# очень понятный пример геттеров и сеттеров и привата

class Product:
    def __init__(self, name, price):
        self.name = name  # Открытый атрибут
        self.__price = price  # Приватный атрибут

    # Геттер для получения значения атрибута price
    @property
    def price(self):
        return self.__price

    # Сеттер для изменения значения атрибута price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной!")
        self.__price = value

# Использование
product = Product("Ноутбук", 50000)

# Доступ к открытому атрибуту
print(product.name)  # Ноутбук

# Попытка получить доступ к приватному атрибуту (будет ошибка)
# print(product.__price)

# Работа с приватным атрибутом через геттер и сеттер
print(product.price)  # 50000
product.price = 45000  # Изменение цены
print(product.price)  # 45000

# Попытка установить некорректную цену
# product.price = -100  # ValueError: Цена не может быть отрицательной!

