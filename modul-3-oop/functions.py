# приветствие
# def greet():
#     print('Hello, world!')
#
# greet()
#
#
# def greet_user(name):
#     print(f'Привет, {name}!')
#
# greet_user('Ann')
# greet_user('Pashka')
#
#
# def sum_numbers(a, b):
#     print(a + b)
#
# sum_numbers(6, 4)


# проверка на четность
# def is_even(number):
#     if number % 2 == 0:
#         print('Четное')
#     else:
#         print('Нечетное')
#
# is_even(int(input('Введите число: ')))


# площадь прямоугольника
# def rectangle_are(weidth, height):
#     if (type(weidth) == float or type(weidth) == int) and (type(height) == float or type(height) == int):
#         if weidth > 0 and height > 0:
#             print('area =', weidth * height)
#         else:
#             print('Некорректные значения')
#     else:
#         print('Неверный тип значений')
#
# rectangle_are(10, 4)


# именованные аргументы, позиционные аргументы, значение по умолчанию
# def format_address(city, street, house_number, apartment=None):
#     address = f"{city}, ул. {street}, д. {house_number}"
#     if apartment is not None:
#         address += f", кв. {apartment}"
#     print(address)
#
# format_address("Москва", "Тверская", 10)
# format_address(city="Санкт-Петербург", street="Невский проспект", house_number=28) #Именованные аргументы
# format_address("Киев", "Крещатик", 5, 12) #Позиционные аргументы, apartment = 12
# format_address("Одесса", house_number=15, street="Дерибасовская") #Комбинирование позиционных и именованных


# приветствие с позиционными и именованными аргументами
# def greet_person(name, age):
#     print(f'Привет, {name}! Тебе {age} лет.')
#
# greet_person('Yulka', 25)
# greet_person(name = 'Pashka', age = 26)
# greet_person(age = 5, name = 'Goshka')


# площадь круга
# def circle_area(r, pi = 3.14159):
#     s = pi * (r ** 2)
#     print(s)
#
# circle_area(3) # здесь pi использовано по умолчанию
# circle_area(3, 3.14) # а здесь передала другое значение для pi


# задание 3 про книги - комбинация аргументов
# def book_info(title, author, year, genre = 'Неизвестно'):
#     print(f'Название: {title}\nАвтор: {author}\nГод издания: {year}\nЖанр: {genre}')
#
# book_info('Война и мир', 'Л.Н. Толстой', 1867, 'драма')
# book_info(author = 'Л.Н. Толстой', year = 1867, title = 'Война и мир', genre = 'драма')
# book_info('Война и мир', 'Л.Н. Толстой', 1867)


# def convert_currency(amount, rate, from_currency="USD", to_currency="EUR"):
#     res = amount * rate
#     print(f'{amount} {from_currency} равно {res} {to_currency}')
#
# convert_currency(10, 0.88)
# convert_currency(200_000, 0.012, 'RUB', 'USD')


#return - сразу прекращает исполнение функции
# def test_return():
#     print("Начало функции")
#     return 10
#     print("Эта строка никогда не будет выполнена.")  # Этот код никогда не выполнится
#     return 20  # Этот код никогда не выполнится
#     print("И эта тоже.")  # Этот код никогда не выполнится
#
# result = test_return()
# print(result)  # Вывод: 10
#
#
# # return
# def add(x, y):
#     result = x + y
#     return result  # Возвращаем сумму
#
# sum_of_numbers = add(5, 3)  # Вызываем функцию и сохраняем результат в переменной
# print(sum_of_numbers)  # Вывод: 8
#
# another_sum = add(-1, 10)
# print(another_sum) # Вывод: 9
#
# print(add(2,7)) # Вывод: 9 - можно сразу напечатать результат


# пример функции которая возвращает кортеж из нескольких значений
# def get_name_and_age():
#     name = "Елена"
#     age = 30
#     return name, age  # Возвращаем кортеж
#
# person_info = get_name_and_age()
# print(person_info)       # Вывод: ('Елена', 30)
# print(person_info[0])    # Вывод: Елена
# print(person_info[1])    # Вывод: 30


# задание 1 - поиск большего числа
# def max_of_two(a, b):
#     if a >= b:
#         return a
#     else:
#         return b
#
# print(max_of_two(5,2))
# print(max_of_two(4, 10))


# задание 2 - длина строки
# def string_length(s):
#     return len(s)
#
# print(string_length('Я хочу спать'))


# калькулятор стоимости доставки

# def calculate_delivery_cost(weight, distance, fragile=False):
#     total_sum = (weight * 10) + (distance * 5)
#     if fragile is True:
#         total_sum *= 1.5
#
#     if total_sum < 200:
#         total_sum = 200
#
#     return total_sum
#
# print(calculate_delivery_cost(10, 10, True))


# анализ списка чисел
# def analyze_numbers(numbers):
#
#     if len(numbers) == 0:
#         return None
#     else:
#         average = sum(numbers) / len(numbers)
#         minimum = min(numbers)
#         maximum = max(numbers)
#
#         even_counter = 0
#         for n in numbers:
#             if n % 2 == 0:
#                 even_counter += 1
#
#
#         analyze_dict = {'Среднее значение': average, 'Минимальное значение': minimum, 'Максимальное значение': maximum,
#                         'Количество четных': even_counter}
#         return analyze_dict
#
# lst = [1,2]
# print(analyze_numbers(lst))


# фильтрация списка по условию
def filter_list(data, threshold):

    result = []
    for e in data:
        if e >= threshold:
            result.append(e)

    return result

lst = [1, 5, 10, 2, 8, 12]
print(filter_list(lst, 7))