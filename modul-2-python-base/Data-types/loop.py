# итерация по списку
# fruits = ["яблоко", "банан", "вишня"]
# for fruit in fruits:
#     print("Фрукт:", fruit)


# итерация по строке
# word = "Python"
# for letter in word:
#     print("Буква:", letter)


# итерация по словарю
# student_grades = {"Аня": 85, "Борис": 90, "Вика": 75}
# for student, grade in student_grades.items():
#     print(student, "получил(а)", grade)


# итерация по множеству
# unique_numbers = {10, 20, 30}
# for number in unique_numbers:
#     print("Число из множества:", number)


# numbers = [10, 20, 30, 40, 50]
# for num in numbers:
#     print('Число =', num)


# text = 'Hello, Python!'
# for l in text:
#     print(l)


# my_tuple = (1, 2, 5)
# for i in my_tuple:
#     print(i)


# my_dudes = {'Sasha': '24', 'Nikita': '24', 'Karina': '25', 'Dima': '25'}
# for name, age in my_dudes.items():
#     print(f'Возраст {name}: {age}')


# ввод данных input
# name = input("Введите ваше имя: ")
# print("Привет,", name)


# age = input("Сколько вам лет? ")
# print("Через 5 лет вам будет", int(age) + 5)


# преобразовать строку input в число
# number = int(input("Введите число: "))
# print("Квадрат числа:", number ** 2)


# обработка ошибок

# try:
#     number = int(input("Введите число: "))
#     print("Квадрат числа:", number ** 2)
# except ValueError:
#     print("Ошибка: нужно вводить только числа!")


# пример - обратный отсчет
# countdown = 5
# while countdown > 0:
#     print("Обратный отсчёт:", countdown)
#     countdown -= 1  # Уменьшаем значение
# print("Поехали!")


# запрос данных до выполнения условия
# user_input = ""
# while user_input != "да":
#     user_input = input("Хотите выйти? (да/нет): ")
# print("Вы вышли из программы.")


# бесконечный цикл
# counter = 0
# while True:
#     print("Итерация:", counter)
#     counter += 1
#     if counter == 3:  # Завершаем бесконечный цикл
#         break


# count = 10
# while count > 0:
#     print(count)
#     count -= 1
# print('Цикл завершен')


# password = input('Введите пароль: ')
# while password != '12345':
#     password = input('Неверно, введите другой пароль: ')
# print('Доступ разрешен')


# num = 1
# while num <= 10:
#     if num % 2 != 0:
#         print(num)
#     num += 1


# оператор break
# for num in range(1, 10):
#     if num == 5:
#         break  # Завершение цикла
#     print(num)


# оператор continue
# for num in range(1, 10):
#     if num == 5:
#         continue  # Пропуск числа 5
#     print(num)


# text = "Hello, Python!"
# vowels = "aeiouyAEIOU"
# count = 0
# for letter in text:
#     if letter in vowels:
#         count += 1
# print(count)


# list = [10, 22, 17, 49, 0, -14, -20, 50, 100, 51, 23, 0, 50, 74]
# for i in list:
#     if i > 50:
#         print(i)
#         break


# a = range(1, 21)
# for num in a:
#     if num % 3 == 0:
#         continue
#     print(num)


# spisok = [10, 20, 30]
# for i in spisok:
#     print(i ** 2)


# day = input('Введите номер дня недели: ')
# if day == '1':
#     print('Monday')
# elif day == '2':
#     print('Thuersday')
# elif day == '3':
#     print('Wednesday')
# elif day == '4':
#     print('Thursday')
# elif day == '5':
#     print('Friday')
# elif day == '6':
#     print('Saturday')
# elif day == '7':
#     print('Sunday')
# else:
#     print('Вы ввели неверное число.')


# day1 = int(input('Введите номер дня недели: '))
# day = (day1 % 7)
# print(day)
# if day == 1:
#     print('Monday')
# elif day == 2:
#     print('Thuersday')
# elif day == 3:
#     print('Wednesday')
# elif day == 4:
#     print('Thursday')
# elif day == 5:
#     print('Friday')
# elif day == 6:
#     print('Saturday')
# elif day == 0:
#     print('Sunday')
# else:
#     print('Вы ввели неверное число.')


# a = 'Pashka Yulka'
# b = ('Pashka\nYulka') # новая строка
# c = ('Pashka\tYulka') # горизонтальная табуляция
# print(a)
# print(b)
# print(c)

# таблица умножения
#Внешний цикл по числам от 1 до 10
#for i in range(1, 11):
    # Вложенный цикл для умножения каждого числа на числа от 1 до 10
#    for j in range(1, 11):
#        print(f"{i} * {j} = {i * j}", end="\t\t")  # Результаты отображаются в строку
#    print()  # Переход на новую строку после внутреннего цикла


# таблица сложения
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(f'{i} + {j} = {i + j}', end='\t')
#     print()


# обработка ошибок в циклах
# обработка деления на ноль
# numbers = [10, 0, 5, 2]

# for num in numbers:
#     try:
#         result = 10 / num
#         print(f"Результат деления: {result}")
#     except ZeroDivisionError:
#         print("Ошибка: Деление на ноль невозможно.")


# ошибка преобразования числа
# data = ["123", "abc", "456", None]
#
# for item in data:
#     try:
#         number = int(item)  # Попытка преобразования строки в число
#         print(f"Число: {number}")
#     except (ValueError, TypeError):
#         print(f"Ошибка: {item} не удалось преобразовать в число.")


# обработка нескольких типов ошибок
# operations = [(10, 2), (5, 0), (8, "string"), (4, 2)]
#
# for a, b in operations:
#     try:
#         result = a / b
#         print(f"Результат: {result}")
#     except ZeroDivisionError:
#         print("Ошибка: Деление на ноль невозможно.")
#     except TypeError:
#         print(f"Ошибка: Неверный тип данных: {b}")


# a = [10, 0, 5, 'abc', 2]
# for i in a:
#     try:
#         print(f'100 / {i} = {100//i}')
#     except ZeroDivisionError:
#         print('Деление на ноль невозможно')
#     except TypeError:
#         print('Неверный формат данных')


# lst = ['123', 'text', None, '456']
# for i in lst:
#     try:
#         x = int(i)
#         print(f'Число: {x}')
#     except (TypeError, ValueError):
#         print(f'{i} не удалось преобразовать в число.')


lst2 = [(10, 5), (3, 0), (7, "str")]

for i, j in lst2:
    try:
        print(f'{i} / {j} = {i/j}')
    except ZeroDivisionError:
        print('Деление на ноль невозможно')
    except TypeError:
        print('Неверный тип данных')