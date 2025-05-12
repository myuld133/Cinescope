# number = 5
#
# if number > 0:
#     print("Число положительное")  # Число положительное
#
# print("продолжаю работу")


# numbers = [1, 2, 3, 4, 5]
#
# if 10 in numbers:
#     print(numbers.index('10'))
# else:
#      print('10 is not in the list')


# number = 2
# if number >= 0:
#     print('Число четное')
# else:
#     print('Число нечетное')


# temperature = 120
#
# if temperature < 0:
#     print("Вода замёрзла (лёд)")
# elif 0 <= temperature < 100:
#     print("Вода жидкая")
# elif temperature == 100:
#     print("Вода закипела")
# else:
#     print("Вода в состоянии пара")


# вложенные if-else
# number = 10
#
# if number > 0:
#     if number % 2 == 0:
#         print("Число положительное и чётное")
#     else:
#         print("Число положительное и нечётное")
# else:
#     print("Число отрицательное или равно нулю")


# number = -15
# if number > 0:
#     if number % 2 == 0:
#         print('Число четное и положительное')
#     else:
#         print('Число нечетное и положительное')
# elif number < 0:
#     if number % 2 == 0:
#         print('Число четное и отрицательное')
#     else:
#         print('Число нечетное и отрицательное')
# else:
#     print('Число равно нулю')


# if 10 > 5:
#     pass  # Ничего не делаем
# else:
#     print("Сработал else!")


# тернарный оператор
# number = 10
# result = "Положительное" if number > 0 else "Неположительное"
# print(result)


# a = 10
# b = 5
# if a > b:
#     print(a)
# elif a < b:
#     print(b)
# else:
#     print ('Числа равны')


used_logins = ["user123", "hacker", "test_bot"]
new_login = 'user123'

if new_login in used_logins:
    print('Такой логин уже зарегистрирован')
else:
    print('Новый логин принят')