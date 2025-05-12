# # создание утилитного класса
# class MathUtils:
#
#     @staticmethod
#     def add(a, b):
#         return a + b
#
#     @staticmethod
#     def multiply(a, b):
#         return a * b
#
#     @staticmethod
#     def is_positive(x):
#         return x > 0
#
#
# # Использование статических методов
# print(MathUtils.add(5, 7))  # Вывод: 12
# print(MathUtils.multiply(3, 4))  # Вывод: 12


# конвертер валют
class CurrencyConverter:

    @staticmethod
    def usd_to_eur(amount):
        eur_amount = amount * 0.85
        return eur_amount

    @staticmethod
    def eur_to_usd(amount):
        usd_amount = amount * 1.18
        return usd_amount

print(CurrencyConverter.usd_to_eur(100))