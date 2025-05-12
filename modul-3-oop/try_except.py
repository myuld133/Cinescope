# обработка разных исключений
# try:
#     value = int(input("Введите число: "))  # Попытка преобразовать ввод пользователя в число
#     result = 10 / value
# except ValueError:  # Если введено не число
#     print("Ошибка: нужно вводить только числа!")
# except ZeroDivisionError:  # Деление на ноль
#     print("Ошибка: деление на ноль!")
# except Exception as e:  # Общее исключение для любых других ошибок
#     print("Произошла ошибка:", e)
# else:  # Блок выполнится, если исключений не было
#     print(f"Результат: {result}")
# finally:  # Этот блок выполнится в любом случае
#     print("Завершение программы.")


# вызов исключений вручную
# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError("На ноль делить нельзя!")  # Генерируем исключение
#     return a / b

# try:
#     print(divide(10, 0))
# except ZeroDivisionError as e:
#     print("Ошибка:", e)

# divide(4, 2)


# функция для деления двух чисел с обработкой исключений
def safe_divide(a, b):
    try:
        res = a / b
    except TypeError:
        print('Неверный тип данных')
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    else:
        print(res)
        return res

# safe_divide(2, '4')


# проверка ввода и чтение файла
def read_file(filename):
    if filename == '':
        raise ValueError('Имя файла не может быть пустым')
    try:
        my_file = open(filename) # открыли файл
        return my_file.read() # прочитали файл и вернули его содержимое
    except FileNotFoundError:
        print(f'Файл {filename} не найден')
        return
    finally:
        print('Закрываем файл')

#print(read_file('hello.txt'))

# проверка деления чисел из списка
def divide_numbers(numbers):
    res_lst = []
    for num in numbers:
        try:
            res = 100 / num
            res_lst.append(res)
            print(res)
        except ZeroDivisionError:
            print('На ноль делить нельзя')
        except TypeError:
            print('Некорректное значение')
    return res_lst


numbers = [2, 10, 0, 'a', -100, None]
print(divide_numbers(numbers))
