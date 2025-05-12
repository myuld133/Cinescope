# задание1
# простые

# a = 4
# b = 2
# print('Сумма: ', a + b)
# print('Разница: ', a - b)
# print('Произведение: ', a * b)
# print('Деление: ', a / b)

# if a > b:
#     print('a больше b')
# elif a < b:
#     print('a меньше b')
# else:
#     print('a равно b')


# средние

# a = 1
# b = 3
# c = 5

# if (a + b) > c:
#     print('Сумма a и b больше c')
# if (a + b) < c:
#     print('сумма a и b меньше c')
# if (a + b) == c:
#     print('сумма a и b равна c')
#
# if (a * b) < c:
#     print('произведение a и b меньше c')
# else:
#     print('нет')


# логические
# n = input('Введите число: ')
# r = range(10, 21)
# print('Входит ли n в диапазон r?', int(n) in r)


# калькулятор
# x = float(input('Введите первое число: '))
# y = float(input('Введите второе число: '))
# try:
#     print(f'{x} // {y} = {x // y}')
# except ZeroDivisionError:
#     print('Деление на ноль невозможно')


# задание 2
# простые

# text = 'Python is awesome!'
# print(text.upper())
# print(text.replace('awesome', 'amazing'))

#text = 'Hello, Python!'
# print(text[:5])
# print(text[::2])

# pi = 3.14159
# print(round(pi, 2))

# средние

# quote = 'Python is easy and powerful!'
# quote2 = quote.replace('easy', 'fun')
# quote3 = quote2.replace('powerful', 'versatile')
# print(quote3)

# name = 'Alice'
# age = '25'
# print(f'{name} is {age} years old.')

# сложное
# data = 'Price: 1234.5678 USD'
# x = float(data[7:16])
# x2 = round(x, 2)
# print(f'Rounded price: {x2} USD')


# задание 3

# простые
# fruits = ["apple", "banana", "cherry", "date"]
# fruits.append('kiwi')
# fruits.remove('banana')
# print(fruits)


# person = {"name": "Alice", "age": 25, "city": "New York"}
# person["age"] = 26
# person["profession"] = "engineer"
# print(person)


# numbers = (10, 20, 30, 40, 50)
# print(numbers[1])


# colors = {"red", "blue", "green"}
# colors.add('yellow')
# colors.remove('blue')
# colors.add('red')
# print(colors)


# r = range(1, 21)
# r_lst = list(r)
# res = sum(r_lst)
# print(res)
# new = []
# for e in r_lst:
#     if e % 3 == 0:
#         new.append(e)
# print(r_lst)
# print(new)


# задание 4

# простое

# for e in range(1,11):
#     print(e)

# r = range(10, 0, -1)
# index = 0
# while index < len(r):
#     print(r[index])
#     index += 1
# print('Счет завершен!')

# n = 1
# while n <= 10:
#     print(f'5 x {n} = {5 * n}')
#     n += 1


itemsToPrice = {'зелье лечения': 100, 'зелье маны': 80, 'свиток скорости': 150, 'артефакт магии': 300}
item = input('Выберите товар: ')

if item in itemsToPrice:
    count = int(input('Введите необходимое количество: '))
    total_sum = itemsToPrice[item] * count
    if total_sum <= 500:
        print('Итого с тебя:', total_sum)
    else:
        print('Итого со скидкой с тебя:', total_sum * 0.8)
else:
    print('У меня такого нет, попробуй в другом месте!')