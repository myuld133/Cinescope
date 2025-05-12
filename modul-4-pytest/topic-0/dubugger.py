# дебагер - пример1
# def calculate_sum(a, b):
#     result = a + b  # Точка остановки здесь
#     return result
#
# x = 5
# y = 10
# total = calculate_sum(x, y)
# print(total)


# #  дебагер - пример2
# def inner_function(x):
#     return x * 2
#
# def outer_function(a):
#     b = inner_function(a + 1)  # Step Over здесь
#     c = b * 3                # После Step Over выполнение будет здесь
#     return c
#
# result = outer_function(5)
# print(result)


# # дебаггер - пример 3
# def func1(x): return x + 1
# def func2(x): return x * 2
# def func3(x): return x**2
#
# result = func1(func2(func3(2))) # Тут несколько вызовов
#
# print(result)


# дебаггер - пример 4
# import requests  # Сторонняя библиотека
#
# def my_function(url):
#     response = requests.get(url)  # Step Into My Code здесь
#     if response.status_code == 200:
#         return response.text
#     else:
#         return "Error"
#
# url = "https://www.example.com"
# content = my_function(url)
# print(content)


# # дебаггер - пример 5
# import requests  # Сторонняя библиотека
#
# def my_function(url):
#     response = requests.get(url)  # брейкпоинт сюда
#     if response.status_code == 200:
#         return response.text
#     else:
#         return "Error"
#
# url = "https://www.example.com"
# content = my_function(url)
# i = "i'm here"
# print(content)


# # упражнение на Step Over и Step Into
# def process_data(data):
#     processed_data = transform_data(data)
#     result = calculate_result(processed_data)
#     return result
#
# def transform_data(data):
#     return [x * 2 for x in data]
#
# def calculate_result(data):
#     return sum(data)
#
# data = [1, 2, 3]
# final_result = process_data(data)
# print(final_result)


# # упражнение step out и просмотр переменных
# def inner(a, b):
#     c = a + b
#     d = c * 2 # Поставьте тут точку останова
#     return d
#
# def outer(x):
#     y = 10
#     z = inner(x, y)
#     return z
#
# result = outer(5)
# print(result)


# упражнение smart step into
def a(x): print("a"); return x + 1
def b(x): print("b"); return x * 2
def c(x): print("c"); return x ** 2

result = a(b(c(2))) # Поставьте тут точку останова
print(result)